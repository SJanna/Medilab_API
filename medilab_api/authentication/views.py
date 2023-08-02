from rest_framework import viewsets, generics
from .models import User, Role, Patient, Doctor, Group
from .serializers import UserSerializer, RoleSerializer, PatientSerializer, DoctorSerializer
# Login imports. ------------------------------------------------ #
from dj_rest_auth.views import LoginView as DefaultLoginView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# --------------------------------------------------------------- #

class LoginView(DefaultLoginView):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:  # if login was successful
            # role = request.user.role.name    # ROLE
            token = response.data.get('key')  # TOKEN
            
            if token:
                # Set token in cookie
                # httponly: cookie can't be accessed by javascript. This is important since we are storing the token in the cookie.
                response.set_cookie('auth_token', token, httponly=True, samesite='Strict', secure=True)
                
            # Adding role to response data. Passing role to frontend.
            # Everytime the role is needed in the frontend, we need to revalidate it with the backend.
            # response.data['role'] = role
            
        return response
    
# create simple view to revalidate the user data in the frontend
class RevalidateUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return JsonResponse(serializer.data)
    
    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    

    

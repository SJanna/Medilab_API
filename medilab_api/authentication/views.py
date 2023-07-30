from dj_rest_auth.views import LoginView as DefaultLoginView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import (BacteriologistUser, BrigadeUser, CompanyUser, DoctorUser,
                     Gender, IdentificationType, OtherUser, PatientUser,
                     ReceptionistUser, Role, UserBase)
from .permissions import (IsBacteriologistUser, IsCompanyUser, IsDoctorUser,
                          IsReceptionistUser, IsSelf)
from .serializers import (BacteriologistSerializer, BrigadeSerializer,
                          CompanySerializer, DoctorSerializer,
                          GenderSerializer, IdentificationTypeSerializer,
                          OtherUserSerializer, PatientSerializer,
                          ReceptionistSerializer, RoleSerializer,
                          UserSerializer)


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
    serializer_class = UserSerializer
    queryset = UserBase.objects.all()
    permission_classes = [IsSelf]
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['username']
    # ordering_fields = ['username']
    # pagination_class = PageNumberPagination
    # pagination_class.page_size = 10


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # ordering_fields = ['created_at', 'updated_at']
    # search_fields = ['name']
    # pagination_class = PageNumberPagination
    # pagination_class.page_size = 2

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer
    queryset = DoctorUser.objects.all()
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['username', 'first_name', 'last_name', 'identification_number']
    # ordering_fields = ['created_at', 'updated_at']
    # pagination_class = PageNumberPagination
    # page_size = 10
    
class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    queryset = CompanyUser.objects.all()


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = PatientUser.objects.all()

class BrigadeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BrigadeSerializer
    queryset = BrigadeUser.objects.all()

class ReceptionistViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ReceptionistSerializer
    queryset = ReceptionistUser.objects.all()

class OtherUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OtherUserSerializer
    queryset = OtherUser.objects.all()

class BacteriologistViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BacteriologistSerializer
    queryset = BacteriologistUser.objects.all()


class IdentificationTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = IdentificationTypeSerializer
    queryset = IdentificationType.objects.all()


class GenderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()


@api_view(['GET'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"detail": "CSRF cookie set"})
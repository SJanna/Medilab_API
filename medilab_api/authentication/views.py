from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsReceptionistUser, IsDoctorUser, IsBacteriologistUser, IsCompanyUser
from .models import UserBase, Group, DoctorUser, CompanyUser, IdentificationType
from .serializers import CompanySerializer, DoctorSerializer, GroupSerializer, IdentificationTypeSerializer, UserSerializer
from rest_framework.response import Response
from dj_rest_auth.views import LoginView as DefaultLoginView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

class LoginView(DefaultLoginView):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:  # if login was successful
            token = response.data.get('key')  # TOKEN
            if token:
                response.set_cookie('auth_token', token, httponly=True, samesite='Strict', secure=True)
        return response

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserBase.objects.all()
    permission_classes = []

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DoctorSerializer
    queryset = DoctorUser.objects.all()

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanySerializer
    queryset = CompanyUser.objects.all()

class IdentificationTypeViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = IdentificationTypeSerializer
    queryset = IdentificationType.objects.all()
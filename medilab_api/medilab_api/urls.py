from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('appointment/', include('appointment.urls')),
    path('exam/', include('exam.urls')),
    path('company/', include('company.urls')),
    path('audit/', include('audit.urls')),
]

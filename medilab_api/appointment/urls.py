from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, AppointmentList, LogEntryList

router = DefaultRouter()
router.register(r'Appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('AppointmentsList/', AppointmentList.as_view()),
    path('LogEntryList/', LogEntryList.as_view()),
]
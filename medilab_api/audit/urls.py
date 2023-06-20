from rest_framework.routers import DefaultRouter
from .views import AuditlogViewSet


router = DefaultRouter()
router.register(r'Auditlog', AuditlogViewSet)

urlpatterns = router.urls

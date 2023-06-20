from rest_framework import viewsets
from auditlog.models import LogEntry
from .serializers import LogEntrySerializer
# Create your views here.

class AuditlogViewSet(viewsets.ModelViewSet):
    serializer_class = LogEntrySerializer
    queryset= LogEntry.objects.all()



from rest_framework import serializers
from auditlog.models import LogEntry


class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        exclude = ['serialized_data', 'additional_data']
        

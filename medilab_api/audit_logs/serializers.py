
from rest_framework import serializers
from auditlog.models import LogEntry
class LogEntrySerializer(serializers.ModelSerializer):
    action = serializers.CharField(source='get_action_display', read_only=True)
    # Nombre del modelo que se está auditando
    content_type = serializers.CharField(source='content_type.model', read_only=True)
    # Info del usuario que realizó el cambio
    actor = serializers.CharField(source='actor.username', read_only=True)
    actor_name = serializers.CharField(source='actor.get_full_name', read_only=True)
    # Formato de changes más legible
    changes = serializers.CharField(source='changes_display_dict', read_only=True)
    # Identificador del objeto que se está auditando
    object_id = serializers.CharField(source='object_pk', read_only=True)
    
    class Meta:
        model = LogEntry
        fields = ['id', 'action', 'content_type', 'actor', 'actor_name', 'timestamp', 'remote_addr', 'additional_data', 'changes', 'object_id']
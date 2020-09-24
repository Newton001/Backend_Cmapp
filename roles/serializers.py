from rest_framework import serializers

from core.models import Role, 


class RoleSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = roles
        fields = ('id','name','date')
        read_only_fields = ('id',)

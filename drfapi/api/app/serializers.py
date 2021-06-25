from rest_framework import serializers
from .models import todos

class todosserializer(serializers.ModelSerializer):
    class Meta:
        model = todos
        fields = "__all__"

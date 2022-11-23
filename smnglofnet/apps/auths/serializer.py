from rest_framework import serializers
from .models import UserNet


class UserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserNet
        fields = ('user', 'first_name', 'last_name')
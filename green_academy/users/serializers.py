from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "date_of_birth"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "date_of_birth"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
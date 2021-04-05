from rest_framework import serializers
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializers(serializers.Serializer):
    email = serializers.EmailField(max_length = 128)
    password = serializers.CharField(max_length=32)

    def create(self, validated_data):
        try:
            email = str(validated_data["email"])
            new_user = User()
            new_user.email = email
            new_user.set_password(validated_data["password"])
            new_user.save()
            return new_user, None

        except KeyError as exc:
            return None, status.HTTP_400_BAD_REQUEST

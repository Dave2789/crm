from rest_framework import serializers
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CustomUser
        fields  = ('id', 'email', 'username', 'last_login', 'first_name', 'last_name', 'date_joined', 'phone_number', 'voice_identifier', 'profile_picture', 'last_access',  )
        #read_only_fields    = ('id', )
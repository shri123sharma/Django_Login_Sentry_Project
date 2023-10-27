from djoser import serializers
from django.contrib.auth import get_user_model
User=get_user_model()

class UserCreateSeralizer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta):
        model=User
        fields=('id','email','first_name','last_name','role','password')
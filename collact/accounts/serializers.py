import re

from rest_framework import serializers
from accounts.models import User, Config


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ('key', 'value')
        read_only_fields = ('key', 'value')


class UserSerializer(serializers.ModelSerializer):
    last_login_dt = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    # AbstractBasicUser를 상속받기 때문
    def get_last_login_dt(self, obj):
        return None

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, user, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()
        return user


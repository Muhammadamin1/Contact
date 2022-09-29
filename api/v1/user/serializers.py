from rest_framework import serializers
from user.models import *


class UserRelativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRelative
        fields = [
            'id',
            'user',
            'full_name',
            'phone_number',
            'email',
            'relative_level',
            'created_at',
            'updated_at',
        ]


class UserRelativeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRelative
        fields = [
            'full_name',
            'phone_number',
            'email',
            'relative_level',
        ]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'phone_number',
            'email',
            'created_at',
            'updated_at',
        ]

    def to_representation(self, instance: User):
        data = super(UserListSerializer, self).to_representation(instance)
        data['relative'] = UserRelativeShortSerializer(instance, context=self.context).data
        return data


class UserCreateSerializer(serializers.ModelSerializer):
    relative = UserRelativeShortSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'phone_number',
            'email',
            'relative',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        validated_user_relative = validated_data.pop('relative')
        user = User.objects.create(**validated_data)
        UserRelative.objects.bulk_create([
            UserRelative(**r, user=user) for r in validated_user_relative
        ])
        return user

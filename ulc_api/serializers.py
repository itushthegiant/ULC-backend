from curses import meta
from rest_framework import serializers

from . import models



class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)


class PropertySerializer(serializers.ModelSerializer):
    """Serializes properties"""

    class Meta:
        model = models.Property
        fields = ('id', 'user_profile', 'name', 'address', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}



class UnitSerializer(serializers.ModelSerializer):
    """Serializes Units"""

    class Meta:
        model = models.Unit
        fields = (
            'id',
            'number',
            'unit_status',
            'operational_status',
            'condition',
            'market_price',
            'sqft',
            'property_id',
            )
        extra_kwargs = {'user_profile': {'read_only': True}}
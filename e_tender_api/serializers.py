from rest_framework import serializers
from e_tender_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API view"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'organization_name', 'email', 'password', 'ntn', 'contact', 'address')
        extra_kwargs= {
            'password': {
                'write_only': True,
                'style': {"input_type": 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            organization_name = validated_data['organization_name'],
            password= validated_data['password'],
            ntn = validated_data['ntn'],
            address = validated_data['address'],
            contact = validated_data['contact']

        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)


         
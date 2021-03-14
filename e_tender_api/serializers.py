from rest_framework import serializers
from e_tender_api import models
from django.http import HttpRequest
import requests
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
            
            organization_name = validated_data['organization_name'],
            password= validated_data['password'],
            email=validated_data['email'],
            ntn = validated_data['ntn'],
            contact = validated_data['contact'],
            address = validated_data['address'],
            

        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)

class ProfileFeeditemSerializer(serializers.ModelSerializer):
    """Serializers profile feed itmes"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }
         
class PublishTenderSerializer(serializers.ModelSerializer):
    """Serializes a tender object"""
    class Meta:
        model =models.Tenders
        fields = ('id', 'organization_name', 'category', 'title', 'availibility', 'region','description','contact','opening_date','last_date','upload')

    def create(self,validated_data):
            tender = models.Tenders(
                organization_name=validated_data['organization_name'],
                title=validated_data['title'],
                availibility=validated_data['availibility'],
                category=validated_data['category'],
                region=validated_data['region'],
                description=validated_data['description'],
                contact=validated_data['contact'],
                opening_date=validated_data['opening_date'],
                last_date=validated_data['last_date'],
                upload= request.FILES.get('file_uploaded',default=''),
                content_type = file_uploaded.content_type
                
            )
            
            tender.save()
            return tender
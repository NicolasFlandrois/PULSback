from rest_framework import serializers
from .models import Customer, Campaign, User
from django.conf import settings


# Serializer pour le model User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        obj = User.objects.create_user(validated_data['username'], '', validated_data['password'])
        obj.customer = validated_data['customer']
        obj.save()
        return obj

# Serializer pour le model Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# Serializer pour le model Campaign
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
from rest_framework import serializers
from .models import Customer, Campaign, User
from terminal.models import Payment
from django.db.models import Sum


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
    logo_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()
    collected = serializers.SerializerMethodField('get_collected')

    class Meta:
        model = Campaign
        fields = '__all__'

    def get_logo_url(self, campaign):
        if campaign.logo:
            if self.context.get('request'):
                request = self.context.get('request')
                logo_url = campaign.logo.url
                return request.build_absolute_uri(logo_url)
            else:
                return campaign.logo.url
        else:
            return campaign.logo

    def get_video_url(self, campaign):
        if campaign.video:
            if self.context.get('request'):
                request = self.context.get('request')
                video_url = campaign.video.url
                return request.build_absolute_uri(video_url)
            else:
                return campaign.video.url
        else:
            return campaign.video

    def get_collected(self, campaign):
        return Payment.objects.filter(campaign=campaign.id, status="Accepted").aggregate(Sum('amount'))['amount__sum'] or 0


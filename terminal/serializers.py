import datetime
from rest_framework import serializers
from .models import Terminal, Donator, Session, Payment
from fleet.models import Campaign
from fleet.serializers import CampaignSerializer


# Serializer pour le model Terminal
class TerminalSerializer(serializers.ModelSerializer):
    campaign = serializers.PrimaryKeyRelatedField(queryset=Campaign.objects.all(), allow_null=True)

    class Meta:
        model = Terminal
        fields = '__all__'


# Serializer pour le model Donator
class DonatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donator
        fields = '__all__'


# Serializer pour le model Payment
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentFullSerializer(serializers.ModelSerializer):
    donator = DonatorSerializer(many=False, read_only=True)
    campaign = CampaignSerializer(many=False, read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


# Serializer pour le model Session
# On surcharge la méthode "Create" pour calculer le timesession
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

    def create(self, validated_data):
        validated_data['timesession'] = validated_data['end_time'] - validated_data['start_time']
        session = Session.objects.create(**validated_data)
        session.save()
        return session

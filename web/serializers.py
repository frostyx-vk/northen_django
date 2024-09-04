from rest_framework import serializers

from .models import (
    Address, ContactInfo, Service, Work, Advantage, Specialization, Technology, OrderPhone, OrderOnline, Partner
)


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ('name', 'description', 'image')


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('name', 'image')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('text',)


class ServiceSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ('name', 'description', 'works', 'price')


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ('title', 'text', 'image')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', 'street', 'house', 'source')


class ContactInfoSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = ContactInfo
        fields = ('phone', 'email', 'telegram', 'address')


class OrderPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPhone
        fields = ('user_phone', 'convenient_time')


class OrderOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderOnline
        fields = ('description', 'user_phone', 'budget')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('image',)

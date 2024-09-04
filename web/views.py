from rest_framework.generics import ListAPIView, CreateAPIView

from .mixins import OrderCreateMixin
from .models import Service, Advantage, ContactInfo, Specialization, Technology, OrderPhone, OrderOnline, Partner
from .serializers import (
    AdvantageSerializer, ContactInfoSerializer, ServiceSerializer, SpecializationSerializer, TechnologySerializer,
    OrderPhoneSerializer, OrderOnlineSerializer, PartnerSerializer
)


class SpecializationListAPIView(ListAPIView):
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()


class TechnologyListAPIView(ListAPIView):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()


class ServiceListAPIView(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class AdvantageListAPIView(ListAPIView):
    serializer_class = AdvantageSerializer
    queryset = Advantage.objects.all()


class ContactInfoListAPIView(ListAPIView):
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all()


class OrderPhoneCreateAPIView(OrderCreateMixin, CreateAPIView):
    serializer_class = OrderPhoneSerializer
    queryset = OrderPhone.objects.all()

    def get_order_params(self, instance):
        return dict(order_phone=instance)


class OrderOnlineCreateAPIView(OrderCreateMixin, CreateAPIView):
    serializer_class = OrderOnlineSerializer
    queryset = OrderOnline.objects.all()

    def get_order_params(self, instance):
        return dict(order_online=instance)


class PartnerListAPIView(ListAPIView):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()

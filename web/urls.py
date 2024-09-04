from django.urls import path

from .views import (
    AdvantageListAPIView, ContactInfoListAPIView, ServiceListAPIView, SpecializationListAPIView, TechnologyListAPIView,
    OrderPhoneCreateAPIView, OrderOnlineCreateAPIView, PartnerListAPIView
)

urlpatterns = [
    path('advantages/', AdvantageListAPIView.as_view()),
    path('contacts/', ContactInfoListAPIView.as_view()),
    path('services/', ServiceListAPIView.as_view()),
    path('specializations/', SpecializationListAPIView.as_view()),
    path('technologys/', TechnologyListAPIView.as_view()),
    path('create-order-phone/', OrderPhoneCreateAPIView.as_view()),
    path('create-order-online/', OrderOnlineCreateAPIView.as_view()),
    path('partners/', PartnerListAPIView.as_view()),
]
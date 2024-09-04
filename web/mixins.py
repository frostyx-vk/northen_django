from rest_framework import status
from rest_framework.response import Response
from django.db import transaction

from web.models import Order


class OrderCreateMixin:
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        order_params = self.get_order_params(instance)
        headers = self.get_success_headers(serializer.data)
        Order.objects.create(user_phone=instance.user_phone, **order_params)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
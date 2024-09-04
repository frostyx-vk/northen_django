from django.core.exceptions import ValidationError
from django.forms import ModelForm


class AddressAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.can_change_order = False
        self.fields['address'].widget.attrs.update({
            'onclick': "window.open('/admin/web/address/', '_blank'); return false;"
        })


class OrderAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_phone'].widget.can_change_order = False
        self.fields['order_phone'].widget.attrs.update({
            'onclick': "window.open('/admin/web/orderphone/', '_blank'); return false;"
        })

    def clean(self):
        cleaned_data = super().clean()
        order_phone = cleaned_data.get('order_phone')
        order_online = cleaned_data.get('order_online')
        if order_phone and order_online:
            raise ValidationError('Ошибка! Указано два типа заказа')
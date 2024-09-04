from django.contrib import admin

from .filters import AddressAutoCompleteFilter
from .forms import AddressAdminForm, OrderAdminForm
from .models import (
    Address, Advantage, ContactInfo, Order, OrderOnline, OrderPhone, Partner, Service, Specialization, Technology, Work
)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('text', )
    search_fields = ('text', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'order')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('text', )
    search_fields = ('text', )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street')
    list_filter = ('city',)
    search_fields = ('city',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')
    form = AddressAdminForm
    list_filter = (AddressAutoCompleteFilter,)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ('user_phone', 'status')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(OrderPhone)
admin.site.register(OrderOnline)

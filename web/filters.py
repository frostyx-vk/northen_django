from admin_auto_filters.filters import AutocompleteFilter


class AddressAutoCompleteFilter(AutocompleteFilter):
    title = 'Адрес'
    field_name = 'address'
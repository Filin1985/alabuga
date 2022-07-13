from django.contrib import admin

from .models import Citizen


class CitizenAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'age',
        'status',
        'master'
    )
    list_editable = ('master',)
    search_fields = ('last_name',)
    list_filter = ('status',)
    empty_value_display = '-пусто-'


admin.site.register(Citizen, CitizenAdmin)

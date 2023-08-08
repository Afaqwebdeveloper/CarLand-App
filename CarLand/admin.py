from django.contrib import admin
from .models import CarBrand, CarModel, Ad

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

class CarBrandAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

class AdAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'get_contact_info', 'date_published')
    list_filter = ('brand', 'model', 'year', 'price')
    search_fields = ('brand__name', 'model__name', 'year', 'contact_info')

    def get_contact_info(self, obj):
        return obj.contact_info
    get_contact_info.short_description = 'Contact Info'

admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(Ad, AdAdmin)

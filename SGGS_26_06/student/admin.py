from django.contrib import admin
from .models import Country,City

# admin.site.register(City)
# admin.site.register(Country)
# admin.site.register(Subject1)




class CountryAdmin(admin.ModelAdmin):


    list_display  = ['name']
    search_fields = ['name']

admin.site.register(Country,CountryAdmin)




class CityAdmin(admin.ModelAdmin):


    list_per_page = 6

    list_display  = ['name','population']
    search_fields = ['name','population']

admin.site.register(City,CityAdmin)


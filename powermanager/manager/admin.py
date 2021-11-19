from django.contrib import admin
# Register your models here.

from manager.models import *

class CountryAdmin(admin.ModelAdmin):
    pass

class RegionAdmin(admin.ModelAdmin):
    pass

class PartyAdmin(admin.ModelAdmin):
    pass

class CorporationAdmin(admin.ModelAdmin):
    pass

class UnionAdmin(admin.ModelAdmin):
    pass

class SectorAdmin(admin.ModelAdmin):
    pass

class ParamilitaryAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country,CountryAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Party,PartyAdmin)
admin.site.register(Corporation,CorporationAdmin)
admin.site.register(Union,UnionAdmin)
admin.site.register(Sector,SectorAdmin)
admin.site.register(Paramilitary,ParamilitaryAdmin)
admin.site.register(Account,AccountAdmin)

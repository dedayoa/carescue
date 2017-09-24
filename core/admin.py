from django.contrib import admin

# Register your models here.
from .models import *

class RequesterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Requester)
admin.site.register(Mechanic)
admin.site.register(TowingCo)
admin.site.register(TowingVehicle)
admin.site.register(QuerySession)
admin.site.register(Query)

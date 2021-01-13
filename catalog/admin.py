from django.contrib import admin

from .models import Technik, Territory, OrderDuration, Order

# Register your models here.
admin.site.register(Technik)
admin.site.register(Territory)
admin.site.register(OrderDuration)
admin.site.register(Order)
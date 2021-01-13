from django.contrib import admin

from .models import Technik, Territory, OrderDuration, Order

# Register your models here.
admin.site.register(Technik)
admin.site.register(Territory)
admin.site.register(OrderDuration)


# admin.site.register(Order)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'phone_number', 'date', 'technik', 'territory', 'duration')
    list_filter = ('date', 'territory')

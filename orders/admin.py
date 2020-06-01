from django.contrib import admin
from django.contrib.admin import AdminSite,ModelAdmin
from django.utils.translation import ugettext_lazy
from . models import  placed_orders ,Regular_Pizza ,Sicilian_Pizza ,Toppings ,Dinner_Platters, Pasta ,Subs, Salads
from django.urls import include, path
from . import views
from django.http import HttpResponse
from django.db import models

class PlacedOrdersAdmin(admin.ModelAdmin):
    model = placed_orders

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('my_admin_path/', views.vieworders, name=view_name),
        ]

# change the name of the header
admin.site.site_header = 'Order Managment'

# Register your models here.
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner_Platters)
admin.site.register(Toppings)
admin.site.register(Sicilian_Pizza)
admin.site.register(Regular_Pizza)
admin.site.register(placed_orders,PlacedOrdersAdmin)

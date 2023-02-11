from django.contrib import admin

# Register your models here.

from .models import Inventory, Transaction

admin.site.register(Inventory)
admin.site.register(Transaction)
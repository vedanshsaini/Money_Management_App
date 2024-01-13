# money_management_app/admin.py

from django.contrib import admin
from .models import Transaction

# Register your models here
admin.site.register(Transaction)

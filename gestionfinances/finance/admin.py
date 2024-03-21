from django.contrib import admin

from .models import Budget
from .models import Transaction


admin.site.register(Budget)
admin.site.register(Transaction)

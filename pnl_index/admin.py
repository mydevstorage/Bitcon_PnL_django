from django.contrib import admin
from .models import *

@admin.register(PnlIndex)
class PnlIndexAdmin(admin.ModelAdmin):
    pass
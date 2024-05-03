from django.contrib import admin
from .models import ManpowerData

class FileAdmin(admin.ModelAdmin):
    list_display = ["id","Seed_RepDate", "Seed_Year"]
    
admin.site.register(ManpowerData, FileAdmin)
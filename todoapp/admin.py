from django.contrib import admin

# Register your models here.
from .models import Plan



class PlanModelAdmin(admin.ModelAdmin):
    list_display=('id','items')

admin.site.register(Plan,PlanModelAdmin)


from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Recruitment)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'reg', 'phone', 'blood', 'address')

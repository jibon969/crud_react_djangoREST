from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp']
    list_per_page = 20

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
from django.contrib import admin
from .models import Employee, Department, Role

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)

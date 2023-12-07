from django.contrib import admin

from django_app_role.models import Permission, Role

admin.site.register(Permission)
admin.site.register(Role)

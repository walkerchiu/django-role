# django_app_account/apps.py

from django.apps import AppConfig


class DjangoAppRoleConfig(AppConfig):
    name = "django_app_role"

    def ready(self):
        pass

from typing import Tuple

from django.db import transaction

from django_app_role import ProtectedPermission
from django_app_role.models import Permission

DJANGO_APP_ORGANIZATION_INSTALLED = (
    importlib.util.find_spec("django_app_organization") is not None
)
if DJANGO_APP_ORGANIZATION_INSTALLED:
    from django_app_organization.models import Organization


class PermissionService:
    @transaction.atomic
    def init_default_data(
        self, organization: Organization
    ) -> Tuple[bool, Permission, Permission]:
        permission_assign_role, _ = Permission.objects.get_or_create(
            organization=organization, slug=ProtectedPermission.AssignRole
        )

        permission_assign_permission, _ = Permission.objects.get_or_create(
            organization=organization, slug=ProtectedPermission.AssignPermission
        )

        return True, permission_assign_role, permission_assign_permission

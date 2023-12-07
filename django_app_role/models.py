import importlib.util
import uuid

from django.db import models

from safedelete.models import SOFT_DELETE_CASCADE

from django_app_core.models import CommonDateAndSafeDeleteMixin, TranslationModel

DJANGO_APP_ORGANIZATION_INSTALLED = (
    importlib.util.find_spec("django_app_organization") is not None
)
if DJANGO_APP_ORGANIZATION_INSTALLED:
    from django_app_organization.models import Organization


class Permission(CommonDateAndSafeDeleteMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    if DJANGO_APP_ORGANIZATION_INSTALLED:
        organization = models.ForeignKey(Organization, models.CASCADE)
    slug = models.CharField(max_length=255, null=True, db_index=True)
    is_protected = models.BooleanField(default=False)

    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        db_table = "app_role_permission"
        get_latest_by = "updated_at"
        if DJANGO_APP_ORGANIZATION_INSTALLED:
            index_together = (("organization", "slug"),)
        ordering = ["id"]

    def __str__(self):
        return str(self.id)


class PermissionTrans(CommonDateAndSafeDeleteMixin, TranslationModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    permission = models.ForeignKey(
        Permission, related_name="translations", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)

    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        db_table = "app_role_permission_trans"
        get_latest_by = "updated_at"
        index_together = (("language_code", "permission"),)
        ordering = ["language_code"]

    def __str__(self):
        return str(self.id)


class Role(CommonDateAndSafeDeleteMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    if DJANGO_APP_ORGANIZATION_INSTALLED:
        organization = models.ForeignKey(Organization, models.CASCADE)
    permissions = models.ManyToManyField(Permission)
    slug = models.CharField(max_length=255, null=True, db_index=True)
    is_protected = models.BooleanField(default=False)

    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        db_table = "app_role_role"
        get_latest_by = "updated_at"
        if DJANGO_APP_ORGANIZATION_INSTALLED:
            index_together = (("organization", "slug"),)
        ordering = ["id"]

    def __str__(self):
        return str(self.id)


class RoleTrans(CommonDateAndSafeDeleteMixin, TranslationModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.ForeignKey(
        Role, related_name="translations", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)

    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        db_table = "app_role_role_trans"
        get_latest_by = "updated_at"
        index_together = (("language_code", "role"),)
        ordering = ["language_code"]

    def __str__(self):
        return str(self.id)

# django_app_role/__init__.py

default_app_config = "django_app_role.apps.DjangoAppRoleConfig"


class ProtectedRole:
    Admin = "admin"
    Collaborator = "collaborator"
    Customer = "customer"
    HQUser = "hq"
    Manager = "manager"
    Member = "member"
    Owner = "owner"
    Partner = "partner"
    Staff = "staff"


class ProtectedPermission:
    AssignRole = "assign_role"
    AssignPermission = "assign_permission"

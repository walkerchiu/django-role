import graphene

from django_app_role.graphql.dashboard.permission import (
    PermissionMutation,
    PermissionQuery,
)
from django_app_role.graphql.dashboard.role import RoleMutation, RoleQuery


class Mutation(
    PermissionMutation,
    RoleMutation,
    graphene.ObjectType,
):
    pass


class Query(
    PermissionQuery,
    RoleQuery,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)

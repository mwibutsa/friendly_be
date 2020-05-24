import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required, staff_member_required

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, username=graphene.String(),
                          email=graphene.String())

    @staff_member_required
    def resolve_users(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        field, value = ('email', email) if email else ('username', username)

        kwargs = {f"{field}": value}

        return get_user_model().objects.filter(**kwargs)

    @login_required
    def resolve_user(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        field, value = ('email', email) if email else ('username', username)

        kwargs = {f"{field}": value}

        return get_user_model().objects.filter(**kwargs).first()

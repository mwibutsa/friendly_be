import graphene
from user import user_schema

import graphql_jwt

class Query(user_schema.query.Query, graphene.ObjectType):
    pass

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(user_schema.query.UserType)

    class Meta:
        excludes = ['password']

    @classmethod
    def resolve(self, root, info, **kwargs):
        return self(user=info.context.user)


class Mutation(user_schema.mutation.Mutation, graphene.ObjectType):
    login = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

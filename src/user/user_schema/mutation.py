from django.contrib.auth import get_user_model
import graphene


class CreateUser(graphene.Mutation):

    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    username = graphene.String()
    password = graphene.String()

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, first_name, last_name, username, password):
        user = get_user_model()(email=email, username=username,
                                first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        # del user.password
        return CreateUser(email=user.email,
                          username=user.username,
                          first_name=user.first_name,
                          last_name=user.last_name)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

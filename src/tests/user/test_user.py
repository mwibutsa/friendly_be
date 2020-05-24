from ..base_config import GraphQLTest
from .user_fixtures import create_user_mutation


class UserProfileTestCase(GraphQLTest):
    """ User profile test cases. """

    def setUp(self):
        super(UserProfileTestCase, self).setUp()

    def test_create_user_account(self):
        response = self.query(create_user_mutation.format(
            firstName="firstName",
            lastName='lastName',
            email="email@gmail.com",
            password='Password@123!',
            username='username'
        ))

        self.assertLess(0, len(response['data']['createUser']))

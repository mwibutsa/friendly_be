from django.test import Client, TestCase

import json

class GraphQLTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.content_type = 'application/json'
        self.url = '/graphql/'

    def query(self, query: str):
        body = dict()
        body['query'] = query

        response = self.client.post(self.url, json.dumps(
            body), content_type=self.content_type)

        content = response.content

        json_response = json.loads(content.decode())

        return json_response

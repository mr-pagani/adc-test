from unittest import TestCase
from app import create_app
from instance.config import app_config
from ...api.v1.models import (MEETUP_LIST, QUESTION_LIST)


class BaseTestCase(TestCase):

    def setUp(self):
        self.app = create_app(config="testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()

    def tearDown(self):
        """removes the dictionaries and the context"""
        del MEETUP_LIST[:]
        del QUESTION_LIST[:]

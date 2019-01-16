import json
from .base_test import BaseTestCase


class TestMeetups(BaseTestCase):

    def test_post_meetups(self):
        '''post a meetup'''
        with self.client:
            response = self.client.post(
                'api/v1/meetups', data=json.dumps(dict(
                    meetup_id=2,
                    createdOn='12 SEP 2019',
                    location='nairobi',
                    images='img.url',
                    topic='interesting topic',
                    happeningOn='15 SEP 2019',
                    tags='INTERESTING'
                )),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 201)


    def test_view_meetups(self):
        with self.client:
            response = self.client.get('/api/v1/meetups')
            x = json.loads(x.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual("meetups not found", x["message"])

    def test_get_meetup_by_id(self):
        with self.client:
            response = self.client.get('/api/v1/meetups/<meetup_id>')
            x = json.loads(x.data)
        self.assertEqual(response.status_code,404)
        self.assertEqual("meetups not found", x["message"])

    def test_view_upcoming_meetups(self):
        with self.client:
            response = self.client.get('/api/v1/meetups/<meetup_id>')
            x = json.loads(x.data)
        self.assertEqual(response.status_code,404)
        self.assertEqual("meetups not found", x["message"])

    def test_delete_meetup(self):
        with self.client:
            response = self.client.get('/api/v1/meetups/<meetup_id>')
            x = json.loads(x.data)
        self.assertEqual(response.status_code,404)
        self.assertEqual("Meetup with the id provided was not found", x["error"])

    def test_create_rsvp(self):
        with self.client:
            response = self.client.get('/api/v1/meetups/<meetup_id>')
            x = json.loads(x.data)
        self.assertEqual(response.status_code,201)
        

from urllib import response
from django.test import TestCase, Client
from django.contrib.auth.models import User
from deposit.views import *
from banksampah.models import News

# Create your tests here.
class LeaderboardTest(TestCase):
    def setUp(self):
        # runs before every test function
        self.dummy_achiever = {
            'name': "test_lb",
            'point': 1903
        }
        self.dummy_comment = {
            'nama': "test_lb",
            'comment': "test_lb"
        }
        self.credentials = {
            'username': 'test_lb',
            'password': 'pebepe123'
        }
        self.user = User.objects.create_user(
            username= self.credentials['username'],
            password= self.credentials['password']
        )
        self.user.save()


    def test_display(self):
        ''' test main /leaderboard/ view without login '''
        c = Client()
        response = c.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_display_logged_in(self):
        ''' test main /leaderboard/ view with login '''
        c = Client()
        response = c.post('/login/', self.credentials, follow=True)
        response = c.get('/leaderboard/')
        is_status_OK = response.status_code == 200
        self.assertTrue(c.session and
                        response and
                        is_status_OK)

    def test_json_lb(self):
        ''' Get raw leaderboard data in JSON from /leaderboard/json. '''
        c = Client()

        redirect = c.get('/leaderboard/json', follow=True)
        status_code = redirect.redirect_chain[0][1]
        self.assertLessEqual(status_code, 400)

    def test_json_logged_in_lb(self):
        c = Client()
        response = c.post('/login/', self.credentials, follow=True)

        # should NOT redirect
        response = c.get('/leaderboard/json/')
        self.assertEqual(response.status_code, 200)

    def test_comments_json_logged_in(self):
        ''' test /json/comments/ to check redirect'''
        c = Client()
        response = c.post('/login/', self.credentials, follow=True)

        # should NOT redirect
        response = c.get('/leaderboard/json/comments/', follow=True)
        self.assertLessEqual(response.status_code, 200)

    def test_submit_comment_logged_in(self):
        '''test submit comments logged in'''
        c = Client()
        c.login(**self.credentials)
        c.post('/login/', self.credentials)
        c.get('/leaderboard/')

        response = c.post('/leaderboard/submit/', self.dummy_comment)
        self.assertEqual(response.status_code, 302) # should be redirect
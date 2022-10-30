from urllib import response
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from deposit.views import *

# Create your tests here.
class DepositTest(TestCase):    
    def setUp(self):
        ''' set up dummy data before EVERY test suite '''
        self.dummy_deposit = {
            'description': "plastic bottles and stuff",
            'type': "PLASTIK",
            'mass': "5.5"
        }
        self.credentials = {
            'username': 'test_user',
            'password': 'pbppbppbp'
        }
        self.user = User.objects.create_user(
            username= self.credentials['username'], 
            password= self.credentials['password']
        )
        self.user.save()
        
    # ------- Test Suites -------
    
    def test_login(self):
        ''' test login process (before utilizing logged-in features)'''
        c = Client()
        is_logged_in = c.login(**self.credentials)
        self.assertTrue(is_logged_in)
        
    def test_view(self):
        ''' Test main /deposit/ view without login '''
        response = Client().get('/deposit/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_logged_in(self):
        c = Client()
        # is_logged_in = c.login(**self.credentials)
        
        response = c.post('/login/', self.credentials, follow=True)
        response = c.get('/deposit/')
        is_status_OK = response.status_code == 200
        self.assertTrue(c.session['is_logged_in'] and 
                        response.context['is_logged_in'] and 
                        is_status_OK)
        
    def test_json(self):
        ''' Get raw deposit data in JSON from /deposit/json. '''
        c = Client()
        
        redirect = c.get('/deposit/json', follow=True)
        status_code = redirect.redirect_chain[0][1]
        self.assertLessEqual(status_code, 400) # should be OK or Redirect
        
    def test_json_logged_in(self):
        c = Client()
        response = c.post('/login/', self.credentials, follow=True)
        
        # should NOT redirect
        response = c.get('/deposit/json/')
        self.assertEqual(response.status_code, 200)
        
    def test_achiever_json(self):
        ''' Test /json/achiever/ to check redirect'''
        c = Client()
        
        redirect = c.get('/deposit/json/achiever', follow=True)
        status_code = redirect.redirect_chain[0][1]
        self.assertLessEqual(status_code, 400) # should be OK or Redirect
        
    def test_achiever_json_logged_in(self):
        ''' Test /json/achiever/ to see if user points can be retrieved'''
        c = Client()
        response = c.post('/login/', self.credentials, follow=True)
        
        redirect = c.get('/deposit/json/achiever', follow=True)
        status_code = redirect.redirect_chain[0][1]
        self.assertEqual(response.status_code, 200)
        
    def test_submit(self):
        ''' Tests if client can submit AND get redirected, without 400/500 code '''
        c = Client()
        c.get('/deposit/')
        
        redirect = c.post('/deposit/submit', self.dummy_deposit, follow=True)
        status_code = redirect.redirect_chain[0][1]
        self.assertEqual(status_code, 301) # should be oK or redirect
        
    def test_submit_logged_in(self):
        ''' Test submitting new deposit'''
        c = Client()
        c.login(**self.credentials)
        c.post('/login/', self.credentials)
        c.get('/deposit/')
        
        response = c.post('/deposit/submit', self.dummy_deposit)
        self.assertEqual(response.status_code, 301) # should be oK or redirect
        
    def test_view_single_deposit_invalid(self):
        c = Client()
        c.login(**self.credentials)
        c.post('/login/', self.credentials)
        c.get('/deposit/')
        
        response = c.get('/deposit/view/1')
        self.assertEqual(response.status_code, 200)
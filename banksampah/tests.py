from django.test import TestCase, Client
from django.contrib.auth.models import User
from deposit.views import *

# Create your tests here.
class HomeTest(TestCase): 
    def setUp(self):
        # runs before every test function
        
        self.credentials = {} #TODO
        user = User.objects.create_user()
    
    def test_home(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_news_json(self):
        c = Client()
        response = c.get("/news/json/")
        self.assertEqual(response.status_code, 200) 
        
    # def test_news_json_logged_in(self):
    #     c = Client()
    #     c.post("/login/", self.credentials)
        
    #     response = c.get("/news/json/")
    #     self.assertEqual(response.status_code, 200) 
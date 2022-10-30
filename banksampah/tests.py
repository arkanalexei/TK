from django.test import TestCase, Client
from django.contrib.auth.models import User
from deposit.views import *
from banksampah.models import News



# Create your tests here.
class HomeTest(TestCase): 
    def setUp(self):
        # runs before every test function
        user = User.objects.create_user(username='test', password='investasibodong')
        userAdmin = User.objects.create_superuser('testAdmin', '', "senjatamakantuan")

    
    def test_home(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_news_json(self):
        c = Client()
        response = c.get("/news/json/")
        self.assertEqual(response.status_code, 200) 

    def test_news(self):
        c = Client()
        c.login(username="test", password="investasibodong")
        response = c.get("/news/")
        self.assertEqual(response.status_code, 200) 
    
    def test_news_read_more(self):
        News.objects.create(title="jamet", description="khatulistiwa")
        c = Client()
        c.login(username="test", password="investasibodong")
        response = c.get("/news/read/1/")
        self.assertEqual(response.status_code, 200) 
from django.test import TestCase, Client
from about.models import Feedback

# Create your tests here.
class AboutTest(TestCase):
    def test_about(self):
        c = Client()
        response = c.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_add_feedback(self):
        c = Client()
        c.login(username="test", password="investasibodong")
        Feedback.objects.create(pengirim="a", message="y", ratings=('5','5'))
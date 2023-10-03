from django.test import TestCase, SimpleTestCase


# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        respones = self.client.get("/")
        self.assertEquals(respones.status_code, 200)

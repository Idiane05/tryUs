from django.test import TestCase
from rest_framework.test import APIClient

class CourseTestCase(TestCase):
    def test_admin_course_creation(self):
        client = APIClient()
        admin_token = 'your_admin_token_here'
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + admin_token)
        valid_course_data = {
            'title': 'Sample Course',
            'description': 'This is a sample course description.',
            'price': 100.00
        }
        response = client.post('/api/courses/', data=valid_course_data)
        self.assertEqual(response.status_code, 201)
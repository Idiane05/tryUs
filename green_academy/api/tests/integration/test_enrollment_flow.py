from django.test import TestCase
from rest_framework.test import APIClient

class EnrollmentIntegrationTest(TestCase):
    def test_full_enrollment_flow(self):
        client = APIClient()
        # 1. User registration
        client.post('/api/users/', {'email': 'student@green.academy', 'password': 'pass123'})
        # 2. Course enrollment
        client.post('/api/enrollments/', {'course_id': 1})
        # 3. Verify enrollment
        response = client.get('/api/enrollments/')
        self.assertEqual(len(response.data['results']), 1)
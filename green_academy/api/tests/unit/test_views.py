from rest_framework.test import APITestCase
from rest_framework import status

class CourseAPITest(APITestCase):
    def test_unauthorized_access(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
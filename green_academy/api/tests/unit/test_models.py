from django.test import TestCase
from users.models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@green.academy", password="testpass123")
        self.assertEqual(user.email, "test@green.academy")
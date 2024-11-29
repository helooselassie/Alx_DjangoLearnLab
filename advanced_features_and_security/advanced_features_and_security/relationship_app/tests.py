from django.test import TestCase
from .models import CustomUser

class CustomUserTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
            date_of_birth="1990-01-01"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("testpassword"))

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword"
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

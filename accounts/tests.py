from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", password="testuserpassword", email="test@mail.com"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@mail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testsuper", email="testsuper@mail.com", password="testsuperpass"
        )

        self.assertEqual(user.username, "testsuper")
        self.assertEqual(user.email, "testsuper@mail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

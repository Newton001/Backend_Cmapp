from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test Creating a new User with an email is successful"""

        email = "test@newton.com"
        password = 'test212312'
        user = get_user_model().object.create_user{
            email = email,
            password=password
        }

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normalized(self):
        email = 'test@gmail.com'
        user = get_user_model().objects.create_user(email, 'test1232com')

        self.assertEqual(user.email.lower)

    def test_new_user_invalid_email(self):
        """Test Ccreating User with no email"""
        with self.assertRaises(alueError):
            get_user_model().objects.create_user(None, '1TESTE12')

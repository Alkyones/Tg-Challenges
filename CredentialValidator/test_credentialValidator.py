import unittest
from credentialValidator import *

class TestCredentialsCheck(unittest.TestCase):

    def test_valid_credentials(self):
        creds = {
            "username": "HelloUser_1",
            "password": "P@ssw0rd",
            "email": "test@gmail.com"
        }
        result = checkCredentials(creds)
        self.assertTrue(result, "Valid credentials should return True")

    def test_invalid_username(self):
        # Test when username contains special characters
        creds1 = {
            "username": "InvalidUsername!@",
            "password": "P@ssw0rd",
            "email": "test@gmail.com"
        }
        result1 = checkCredentials(creds1)
        self.assertFalse(result1, "Invalid username should return False")

        # Test when username starts with a number
        creds2 = {
            "username": "123Username",
            "password": "P@ssw0rd",
            "email": "test@gmail.com"
        }
        result2 = checkCredentials(creds2)
        self.assertFalse(result2, "Username starting with a number should return False")

    def test_invalid_password(self):
        # Test when password is too long
        creds1 = {
            "username": "HelloUser_1",
            "password": "VeryLongPassword123456789",
            "email": "test@gmail.com"
        }
        result1 = checkCredentials(creds1)
        self.assertFalse(result1, "Too long password should return False")

        # Test when password contains the username
        creds2 = {
            "username": "HelloUser_1",
            "password": "HelloUser_1_Password",
            "email": "test@gmail.com"
        }
        result2 = checkCredentials(creds2)
        self.assertFalse(result2, "Password containing username should return False")

    def test_invalid_email(self):
        # Test when email is not in a valid format
        creds1 = {
            "username": "HelloUser_1",
            "password": "P@ssw0rd",
            "email": "invalid_email"
        }
        result1 = checkCredentials(creds1)
        self.assertFalse(result1, "Invalid email should return False")

        # Test when email is missing the "@" symbol
        creds2 = {
            "username": "HelloUser_1",
            "password": "P@ssw0rd",
            "email": "testgmail.com"
        }
        result2 = checkCredentials(creds2)
        self.assertFalse(result2, "Email without @ symbol should return False")

    def test_empty_credentials(self):
        # Test when credentials dictionary is empty
        creds = {}
        result = checkCredentials(creds)
        self.assertFalse(result, "Empty credentials should return False")

    def test_username_length(self):
        # Test when username is too long
        creds = {
            "username": "VeryLongUsername123456",
            "password": "P@ssw0rd",
            "email": "test@gmail.com"
        }
        result = checkCredentials(creds)
        self.assertFalse(result, "Too long username should return False")

    def test_valid_email(self):
        # Test with a valid email address
        creds = {
            "username": "HelloUser_1",
            "password": "P@ssw0rd",
            "email": "test@gmail.com"
        }
        result = checkCredentials(creds)
        self.assertTrue(result, "Valid email should return True")

if __name__ == '__main__':
    unittest.main()

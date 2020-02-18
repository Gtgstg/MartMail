import unittest
from app import app
from unittest import mock
class FlaskTestCase(unittest.TestCase):
    def test_users(self):
        tester=app.test_client(self)
        response=tester.get('/users',method=['GET'])
        self.assertEqual(response.status_code,200)

if __name__=='__main__':
    unittest.main()
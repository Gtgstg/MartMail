import unittest
from app.routes import hello_world
from app.routes import getting_user
from app.routes import deleting_user
from app.routes import putting_user
from app.routes import posting_user
from unittest.mock import patch

class BasicTests(unittest.TestCase):
    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_get(self, mock_get):
        mock_get.return_value.status_code = 200
        response = getting_user("shanu")
        self.assertEqual(response, "shanu@gmail.com")

    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_get(self, mock_get):
        mock_get.return_value.status_code = 200
        response = hello_world()
        self.assertEqual(response, "Hello-world")

    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_delete(self, mock_delete):
        mock_delete.return_value.status_code = 200
        response = deleting_user("cust")
        self.assertEqual(response, 'success deletion with customername {}'.format("cust"))

    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_put(self, mock_put):
        mock_put.return_value.status_code = 200
        response = putting_user("cust@gmail.com", "cust")
        response='updated  id is cust@gmail.com'
        self.assertEqual(response, 'updated  id is cust@gmail.com')

    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_post(self, mock_post):
        mock_post.return_value.status_code = 200
        response = posting_user("cust", "cust@gmail.com", 0)
        self.assertEqual(response, "cust")

    # @patch('app.routes.requests.get')
    # def test_request_response_with_decorator_for_post(self, mock_post):
    #     mock_post.return_value.status_code = 200
    #     response=0
    #     try:
    #         response = csvRead()
    #     except:
    #         response='File Received'
    #     self.assertEqual(response, 'File Received')

if __name__ == "__main__":
    unittest.main()
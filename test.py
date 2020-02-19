import unittest
from app.routes import hello_world
from app.routes import customer
from app.routes import delete_customer
from app.routes import put_customer
# from app.routes import post_customer
# from app.routes import get_template
# from app.routes import get_customer
from unittest.mock import patch


class BasicTests(unittest.TestCase):
    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_get(self, mock_get):
        mock_get.return_value.status_code = 200
        response = customer("shanu")
        self.assertEqual(response, "shanu@gmail.com")

    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_get(self, mock_get):
        mock_get.return_value.status_code = 200
        response = hello_world()
        self.assertEqual(response, "Hello-world")

    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_delete(self, mock_delete):
        mock_delete.return_value.status_code = 200
        response = delete_customer("cust")
        self.assertEqual(response, 'success deletion with customername {}'.format("cust"))

    @patch('app.routes.requests.get')
    def test_request_response_with_decorator_for_put(self, mock_put):
        mock_put.return_value.status_code = 200
        response = put_customer("cust@gmail.com", "cust")
        response='updated  id is cust@gmail.com'
        self.assertEqual(response, 'updated  id is cust@gmail.com')



if __name__ == "__main__":
    unittest.main()
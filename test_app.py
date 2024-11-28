import unittest
from app import app  # Import your app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True  # Enables testing mode

    def test_home(self):
        # Send a GET request to the '/' route
        response = self.app.get('/')
        
        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the JSON response matches the expected output
        self.assertEqual(response.get_json(), {"message": "Hello my name is obi jnr"})

# Run the tests
if __name__ == '__main__':
    unittest.main()

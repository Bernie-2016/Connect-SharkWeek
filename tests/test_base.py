import unittest

from .base import BaseTestCase


class TestMain(BaseTestCase):

    def test_index(self):
        # Ensure Flask is setup.
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{\n  "status": "OK"\n}', response.data)

if __name__ == '__main__':
    unittest.main()

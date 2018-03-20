import unittest
import json

import fib


class FibTestCase(unittest.TestCase):

    def setUp(self):
        fib.app.testing = True
        self.app = fib.app.test_client()

    def test_fib_num(self):
        rv = self.app.get('/fib/3')
        self.assertEquals(json.loads(rv.data), [0, 1, 1])

        rv = self.app.get('/fib/6')
        self.assertEquals(json.loads(rv.data), [0, 1, 1, 2, 3, 5])

    def test_fib_neg_num(self):
        rv = self.app.get('/fib/-3')
        self.assertEquals(rv.status_code, 404)


if __name__ == "__main__":
    unittest.main()

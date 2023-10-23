import unittest

import HttpRequest as ht
import requests


class MyTestCase(unittest.TestCase):
    def setUp(self, url = "https://www.google.com"):
        self.ht_ = ht.myHttpRequest(url)

    def test_getHttpRequest(self):
        status_code = self.ht_.get_http_request()
        print(f"Status Code: {status_code}")

        assert 200 == status_code


if __name__ == '__main__':
    unittest.main()

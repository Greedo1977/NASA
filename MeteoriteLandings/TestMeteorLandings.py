import unittest

import HttpRequest as ht
import Meteor as mt
import requests


class TestMeteorLandings(unittest.TestCase):
    def setUp(self, url = "https://www.google.com"):
        self.ht_ = ht.myHttpRequest(url)
        self.m = mt.Meteor(name='Aachen', id='23', recclass='10', latitude='20.20', longitude='20.20', year='2020', mass='30')

    def test_getHttpRequest(self):
        status_code = self.ht_.get_http_request()
        assert 200 == status_code

    def test_metor_print(self):
        s = 'Name: Aachen Id: 23 Recclass: 10 Latitude: 20.20 Longitude: 20.20 Year: 2020 Mass: 30'
        assert (self.m.__str__() == s)

if __name__ == '__main__':
    unittest.main()

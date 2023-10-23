import requests

class myHttpRequest:
    def __init__(self, url):
        self.url_ = url
        self.response_ = None
        self.requests_ = None

    def get_http_request(self):
        statuscode = 0
        try:
            self.response_ = requests.get(self.url_)
        except self.requests_.exceptions.ConnectionError:
            print('***** Connection Error *****')
        except self.requests_.exceptions.Timeout:
            print('***** Timeout Error *****')
        else:
            return self.response_.status_code

    def get_json(self):
        return self.response_.json()


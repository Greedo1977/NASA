import sys
import HttpRequest as ht
import requests

def main() -> int:
    """Echo the input arguments to standard output"""
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    myRequest = ht.myHttpRequest(url)

    myRequest.get_http_request()
    js = myRequest.get_json()
    print(js)

    return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
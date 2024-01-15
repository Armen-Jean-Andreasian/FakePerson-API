import requests
from config import get_endpoint_urls


def test_endpoints():
    endpoint_urls = get_endpoint_urls()

    for url in endpoint_urls:
        response = requests.get(url)
        status_code = response.status_code
        print(url, status_code)
        print(response.json())
        assert response.json() and status_code == 200


if __name__ == '__main__':
    test_endpoints()


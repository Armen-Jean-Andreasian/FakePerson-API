endpoint_passport = "/passport_data"
endpoint_all_data = "/all_data"
endpoint_personal_data = "/personal_data"


def get_endpoints() -> tuple:
    """Returns a tuple of available endpoints"""
    return endpoint_passport, endpoint_personal_data, endpoint_all_data

def get_endpoint_urls(domain: str = None, port: str = None, country: str = None) -> list:
    """
    Returns custom/default URL implementations of endpoints in a list.

    Return example with given params:
        ['domain:port/country/passport_data', 'domain:port/country/all_data', 'domain:port/country/personal_data']
    *
    Return example with no given params:
        ['http://127.0.0.1:8000/France/passport_data', 'http://127.0.0.1:8000/France/all_data', 'http://127.0.0.1:8000/France/personal_data']
    """
    DOMAIN = "http://127.0.0.1" if domain is None else domain
    PORT = ":8000" if port is None else port
    COUNTRY = "/France" if country is None else country

    global endpoint_passport, endpoint_personal_data, endpoint_all_data

    return [
        DOMAIN + PORT + COUNTRY + endpoint for endpoint in (endpoint_passport, endpoint_all_data, endpoint_personal_data)
    ]

import requests
from requests.exceptions import ConnectionError


def get_facts():
    try:
        response = requests.get("http://catfacts-api.appspot.com/api/facts")
    except ConnectionError:
        print("No connection")
        return None
    code = response.status_code
    print(code)
    if 200 == code:
        print("Test Pass")
    else:
        print("Test Fail")

    # fact = response.json()

    # text = fact["facts"]
    # print("***" + text[0].upper() + "*****")


get_facts()

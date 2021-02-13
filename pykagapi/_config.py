import requests
import json

LIBRARY_NAME = "pykagapi"
SESSION = requests.Session()
SESSION.headers.update({"user-agent": LIBRARY_NAME})
TIMEOUT = 30

#Will probably move it somewhere else, at some point
def get_content(url):
    '''Recives str(url). Fetches info from it via get() method of requests.Session()
    Then checks if response's code wasnt the one of error.
    If everyting ok - returns response.content'''

    answer = SESSION.get(url, timeout = TIMEOUT)
    answer.raise_for_status()
    data = answer.content

    return data

def get_data(url, auth = None):
    '''Recives str(url). Optionally receives auth(login, password).
    Fetches info from specified url via get() method of requests.Session.
    Then checks if response's code wasnt the one of error.
    If everyting ok - returns response.text'''
    if auth:
        answer = SESSION.get(url, auth=(login, password), timeout = TIMEOUT)
    else:
        answer = SESSION.get(url, timeout = TIMEOUT)
    answer.raise_for_status()
    data = answer.text

    return data

def get_dictionary(url):
    '''Redirects specified url to be fetched by get_data().
    Threats received data as json, converts it into python dictionary and returns'''

    json_data = get_data(url)
    data = json.loads(json_data)

    return data

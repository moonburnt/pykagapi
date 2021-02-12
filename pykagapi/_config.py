import requests

LIBRARY_NAME = "pykagapi"
SESSION = requests.Session()
SESSION.headers.update({"user-agent": LIBRARY_NAME})
TIMEOUT = 30

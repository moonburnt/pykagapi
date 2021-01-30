import requests
import json
import logging

log = logging.getLogger(__name__)

api_url = "https://api.kag2d.com/v1/player"
timeout = 30

#Player shenanigans
def full_info(nickname):
    '''Receives player's nickname (str), returns dictionary with player's total info'''
    log.debug(f"Attempting to get {nickname}'s complete player info")
    url = f"{api_url}/{nickname}"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pydata = json.loads(data.text)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def info(nickname):
    '''Receives player's nickname (str), returns dictionary with player's general info'''
    log.debug(f"Attempting to get {nickname}'s player info")
    url = f"{api_url}/{nickname}/info"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['playerInfo']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def status(nickname):
    '''Receives player's nickname (str), returns dictionary with player's status'''
    log.debug(f"Attempting to get {nickname}'s player status")
    url = f"{api_url}/{nickname}/status"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['playerStatus']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def bans(nickname):
    '''Receives player's nickname (str), returns dictionary with player's banflags'''
    log.debug(f"Attempting to get {nickname}'s banflags")
    url = f"{api_url}/{nickname}/banflags"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['playerBanFlags']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def private_info(login, password, nickname=None):
    '''Receives your (unless you are admin) login, password, nickname (strs), returns dictionary with private info'''
    if not nickname:
        nickname = login
    log.debug(f"Attempting to get {nickname}'s private info")
    url = f"{api_url}/{nickname}/myinfo"
    data = requests.get(url, auth=(login, password), timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['playerInfoPrivate']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def forum_info(login, password, nickname=None):
    '''Receives your (unless you are admin) login, password, nickname (strs), returns dictionary with private forum info'''
    if not nickname:
        nickname = login
    log.debug(f"Attempting to get {nickname}'s private forum info")
    url = f"{api_url}/{nickname}/foruminfo"
    data = requests.get(url, auth=(login, password), timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['playerInfoForum']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def avatar(nickname, size="m"):
    '''Receives player's nickname and avatar size ("s", "m" or "l"), returns str link to profile picture of that size'''
    log.debug(f"Attempting to get {nickname}'s profile picture of size {size}")
    url = f"{api_url}/{nickname}/avatar/{size}"
    data = requests.get(url, timeout = timeout)
    pd = json.loads(data.text)
    pydata = str(list(pd.values())[0])
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def avatars(nickname):
    '''Receives str(nickname), returns dictionary with links to large, medium and small pfps'''
    log.debug(f"Attempting to get {nickname}'s profile pictures")
    url = f"{api_url}/{nickname}/avatar/"
    data = requests.get(url, timeout = timeout)
    pydata = json.loads(data.text)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

#Token shenanigans
def token(login, password):
    '''Receives player's login and password (str), returns player's authentication token (str)'''
    log.debug(f"Attempting to get {login}'s authentication token")
    url = f"{api_url}/{login}/token/new"
    data = requests.get(url, auth=(login, password), timeout = timeout)
    pd = json.loads(data.text)
    pydata = str(pd['playerToken'])
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def verify_token(username, token):
    '''Receives username and token. Verifies if token is valid for that person. Returns True if its valid'''
    log.debug(f"Attempting to verify {login}'s authentication token")
    url = f"{api_url}/{username}/token/{token}"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    log.debug(f"{token} is valid token")
    return True

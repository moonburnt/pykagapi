import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://api.kag2d.com/v1/player"
get_dictionary = _config.get_dictionary

#Player shenanigans
def full_info(nickname):
    '''Receives player's nickname (str).
    Returns dictionary with complete player's info'''
    log.debug(f"Attempting to get {nickname}'s complete player info")
    url = f"{API_URL}/{nickname}"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def info(nickname):
    '''Receives player's nickname (str).
    Returns dictionary with player's general info'''
    log.debug(f"Attempting to get {nickname}'s player info")
    url = f"{API_URL}/{nickname}/info"
    pd = get_dictionary(url)
    pydata = pd['playerInfo']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def status(nickname):
    '''Receives player's nickname (str).
    Returns dictionary with player's status'''
    log.debug(f"Attempting to get {nickname}'s player status")
    url = f"{API_URL}/{nickname}/status"
    pd = get_dictionary(url)
    pydata = pd['playerStatus']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def bans(nickname):
    '''Receives player's nickname (str).
    Returns dictionary with player's banflags'''
    log.debug(f"Attempting to get {nickname}'s banflags")
    url = f"{API_URL}/{nickname}/banflags"
    pd = get_dictionary(url)
    pydata = pd['playerBanFlags']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def private_info(login, password, nickname=None):
    '''Receives str(login) and str(password). Optionally receives str(nickname).
    With nickname - will return dictionary with private info of that player.
    Without - returns dictionary with your private info'''
    if not nickname:
        nickname = login
    log.debug(f"Attempting to get {nickname}'s private info")
    url = f"{API_URL}/{nickname}/myinfo"
    pd = get_dictionary(url, (login, password))
    pydata = pd['playerInfoPrivate']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def forum_info(login, password, nickname=None):
    '''Receives str(login) and str(password). Optionally receives str(nickname).
    With nickname - will return dictionary with private forum info of that player.
    Without - returns dictionary with your private forum info'''
    if not nickname:
        nickname = login
    log.debug(f"Attempting to get {nickname}'s private forum info")
    url = f"{API_URL}/{nickname}/foruminfo"
    pd = get_dictionary(url, (login, password))
    pydata = pd['playerInfoForum']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def avatar(nickname, size="m"):
    '''Receives player's nickname. Optionally receives avatar size ("s", "m", "l").
    Returns link to profile picture of that size.
    If size not specified - returns link to medium-sized picture'''
    log.debug(f"Attempting to get {nickname}'s profile picture of size {size}")
    url = f"{API_URL}/{nickname}/avatar/{size}"
    pd = get_dictionary(url)
    pydata = str(list(pd.values())[0])
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def avatars(nickname):
    '''Receives str(nickname). Returns dict with links to player's pfp of different sizes'''
    log.debug(f"Attempting to get {nickname}'s profile pictures")
    url = f"{API_URL}/{nickname}/avatar/"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

#Token shenanigans
def token(login, password):
    '''Receives str(login), str(password).
    Returns str(player's auth token)'''
    log.debug(f"Attempting to get {login}'s authentication token")
    url = f"{API_URL}/{login}/token/new"
    pd = get_dictionary(url, (login, password))
    pydata = str(pd['playerToken'])
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def verify_token(username, token):
    '''Receives username and token. Verifies if token is valid for that person.
    Returns True if its valid, false otherwise'''
    log.debug(f"Attempting to verify {login}'s authentication token")
    url = f"{API_URL}/{username}/token/{token}"
    try:
        pd = get_dictionary(url)
    except:
        log.debug(f"{token} is invalid token")
        return False
    else:
        log.debug(f"{token} is valid token")
        return True

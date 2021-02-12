import requests
import json
import logging
from pykagapi import _config

log = logging.getLogger(__name__)

api_url = "https://api.kag2d.com/v1"
TIMEOUT = _config.TIMEOUT
SESSION = _config.SESSION

def api_info():
    '''Returns dictionary with general info about this api'''
    log.debug(f"Attempting to get info about this api")
    data = SESSION.get(api_url, timeout = TIMEOUT)
    data.raise_for_status()
    pydata = json.loads(data.text)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def game_info():
    '''Returns dictionary with general info about KAG'''
    log.debug(f"Attempting to get info about this game")
    url = f"{api_url}/game/thd/kag"
    data = SESSION.get(url, timeout = TIMEOUT)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['gameInfo']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def my_ip():
    '''Receive your IP (str) from kag api'''
    log.debug(f"Attempting to get your IP from api")
    url = f"{api_url}/myip"
    data = SESSION.get(url, timeout = TIMEOUT)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['yourIP']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

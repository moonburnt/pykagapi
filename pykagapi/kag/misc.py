import requests
import json
import logging

log = logging.getLogger(__name__)

api_url = "https://api.kag2d.com/v1"
timeout = 30

def api_info():
    '''Returns dictionary with general info about this api'''
    log.debug(f"Attempting to get info about this api")
    data = requests.get(api_url, timeout = timeout)
    data.raise_for_status()
    pydata = json.loads(data.text)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def game_info():
    '''Returns dictionary with general info about KAG'''
    log.debug(f"Attempting to get info about this game")
    url = f"{api_url}/game/thd/kag"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['gameInfo']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def my_ip():
    '''Receive your IP (str) from kag api'''
    log.debug(f"Attempting to get your IP from api")
    url = f"{api_url}/myip"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['yourIP']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

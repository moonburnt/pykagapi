import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://api.kag2d.com/v1"
get_dictionary = _config.get_dictionary

def api_info():
    '''Returns dictionary with general info about this api'''
    log.debug(f"Attempting to get info about this api")
    url = API_URL
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def game_info():
    '''Returns dictionary with general info about KAG'''
    log.debug(f"Attempting to get info about this game")
    url = f"{API_URL}/game/thd/kag"
    pd = get_dictionary(url)
    pydata = pd['gameInfo']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def my_ip():
    '''Receive your IP (str) from kag api'''
    log.debug(f"Attempting to get your IP from api")
    url = f"{API_URL}/myip"
    pd = get_dictionary(url)
    pydata = pd['yourIP']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

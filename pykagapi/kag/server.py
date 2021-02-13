import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://api.kag2d.com/v1/game/thd/kag/server/"
get_dictionary = _config.get_dictionary
get_content = _config.get_content

def status(ip, port):
    '''Receives ip and port, returns dictionary with server's info'''
    log.debug(f"Attempting to get {ip}:{port}'s server info")
    url = f"{API_URL}/{ip}/{port}/status"
    pd = get_dictionary(url)
    pydata = pd['serverStatus']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def minimap(ip, port):
    '''Receives ip and port, returns server's current map image in binary form.
    Use something like pillow+BytesIO to decode it and see afterwards'''
    log.debug(f"Attempting to get {ip}:{port}'s minimap")
    url = f"{API_URL}/{ip}/{port}/minimap"
    data = get_content(url)
    log.debug(f"Got minimap in binary form")
    return data

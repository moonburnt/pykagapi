import requests
import json
import logging

log = logging.getLogger(__name__)

api_url = "https://api.kag2d.com/v1/game/thd/kag/server/"
timeout = 30

def status(ip, port):
    '''Receives ip and port, returns dictionary with server's info'''
    log.debug(f"Attempting to get {ip}:{port}'s server info")
    url = f"{api_url}/{ip}/{port}/status"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['serverStatus']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def minimap(ip, port):
    '''Receives ip and port, returns server's current map image in binary form (use something like Pillow+BytesIO to decode it)'''
    log.debug(f"Attempting to get {ip}:{port}'s minimap")
    url = f"{api_url}/{ip}/{port}/minimap"
    data = requests.get(url, timeout = timeout)
    log.debug(f"Got minimap in binary form")
    return data.content

import requests
import json
import logging

log = logging.getLogger(__name__)

api_url = "https://api.kag2d.com/v1/game/1/servers"
timeout = 30

def filters():
    '''Receive dic(info) with valid filters used in server-related requests'''
    log.debug(f"Attempting to get info about valid filters for server requests")
    url = f"{api_url}/filterinfo"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['serverListFilterFields']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def serverlist(filters=None):
    '''Optionally receives list(filters). Returns list with matching servers (or all known servers, if used without filter). May take a while to process'''
    if filters:
        log.debug(f"Attempting to get list of servers that match filters: {filters}")
        jfilters = json.dumps(filters)
        url = f"{api_url}?filters={jfilters}"
    else:
        log.debug(f"Attempting to get complete serverlist. May take a while")
        url = f"{api_url}"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['serverList']
    log.debug(f"Gathered info about {len(pydata)} servers")
    return pydata

def alive():
    '''Returns list with servers thats up and running. Or at least according to api'''
    log.debug(f"Attempting to get list of currently working servers")
    filters = [{'field': 'current', 'op': 'eq', 'value': True}]
    pydata = serverlist(filters)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def active():
    '''Returns list with servers that contain players'''
    log.debug(f"Attempting to get list of servers that currently have players")
    filters = [{'field': 'current', 'op': 'eq', 'value': True}, {'field': 'currentPlayers', 'op': 'ge', 'value': 1}]
    pydata = serverlist(filters)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

import json
import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://api.kag2d.com/v1/game/1/servers"
get_dictionary = _config.get_dictionary

def filters():
    '''Receive dic(info) with valid filters used in server-related requests'''
    log.debug(f"Attempting to get info about valid filters for server requests")
    url = f"{API_URL}/filterinfo"
    pd = get_dictionary(url)
    pydata = pd['serverListFilterFields']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def serverlist(filters=None):
    '''Optionally receives list(filters). Returns list with matching servers.
    Without filter - will return all known servers. May take a while to process'''
    if filters:
        log.debug(f"Attempting to get servers that match filters: {filters}")
        jfilters = json.dumps(filters)
        url = f"{API_URL}?filters={jfilters}"
    else:
        log.debug(f"Attempting to get complete serverlist. May take a while")
        url = f"{API_URL}"
    pd = get_dictionary(url)
    pydata = pd['serverList']
    log.debug(f"Gathered info about {len(pydata)} servers")
    return pydata

def alive():
    '''Returns list of servers thats up and running, according to api'''
    log.debug(f"Attempting to get list of currently working servers")
    filters = [{'field': 'current', 'op': 'eq', 'value': True}]
    pydata = serverlist(filters)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def active():
    '''Returns list of servers with players on them'''
    log.debug(f"Attempting to get list of servers that currently have players")
    filters = [{'field': 'current', 'op': 'eq', 'value': True},
               {'field': 'currentPlayers', 'op': 'ge', 'value': 1}]
    pydata = serverlist(filters)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

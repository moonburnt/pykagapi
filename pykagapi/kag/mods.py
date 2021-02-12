import requests
import json
import logging
from pykagapi import _config

log = logging.getLogger(__name__)

api_url = "https://api.kag2d.com/v1/game/thd/kag/mods"
TIMEOUT = _config.TIMEOUT
SESSION = _config.SESSION

def modlist(filters = None):
    '''Optionally receives list(filters), returns list with matching (or all, if nothing has been passed) registered mods (but nobody bothers to do that anymore, so its not that long)'''
    if filters:
        log.debug(f"Attempting to get list of mods that match filters: {filters}")
        jfilters = json.dumps(filters)
        url = f"{api_url}?filters={jfilters}"
    else:
        log.debug(f"Attempting to get complete modlist")
        url = f"{api_url}"
    data = SESSION.get(url, timeout = TIMEOUT)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['modList']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def filters():
    '''Returns list of valid filters to be used with get_mod_list()'''
    log.debug(f"Attempting to get info about valid filters for mod requests")
    url = f"{api_url}/filterinfo"
    data = SESSION.get(url, timeout = TIMEOUT)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['modListFilterFields']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

import json
import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://api.kag2d.com/v1/game/thd/kag/mods"
get_dictionary = _config.get_dictionary

def modlist(filters = None):
    '''Optionally receives list(filters), returns list with matching registered mods.
    Without filter - will return all registered mods.
    Since nobody bothers to do register these anymore, it wont take that long'''
    if filters:
        log.debug(f"Attempting to get list of mods matching filters: {filters}")
        jfilters = json.dumps(filters)
        url = f"{API_URL}?filters={jfilters}"
    else:
        log.debug(f"Attempting to get complete modlist")
        url = f"{API_URL}"
    pd = get_dictionary(url)
    pydata = pd['modList']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def filters():
    '''Returns list of valid filters to be used with get_mod_list()'''
    log.debug(f"Attempting to get info about valid filters for mod requests")
    url = f"{API_URL}/filterinfo"
    pd = get_dictionary(url)
    pydata = pd['modListFilterFields']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

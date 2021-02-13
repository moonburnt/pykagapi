import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://kagstats.com/api/kills"
get_dictionary = _config.get_dictionary

def recent():
    '''Returns list of recent 100 kills across all servers tracked by api'''
    log.debug("Attempting to get list of recent kills")
    url = API_URL
    pd = get_dictionary(url)
    pydata = pd['values']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def kill_info(kill_id):
    '''Receives str or int(kill id), returns dict with info about that kill'''
    log.debug(f"Attempting to get info about kill under id {kill_id}")
    url = f"{API_URL}/{kill_id}"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

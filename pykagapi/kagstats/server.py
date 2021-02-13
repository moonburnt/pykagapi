import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://kagstats.com/api/servers"
get_dictionary = _config.get_dictionary

def serverlist():
    '''Returns list of up and running servers, tracked by this instance of api'''
    log.debug("Attempting to get list of servers tracked by kagstats api")
    url = API_URL
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def info(server_id):
    '''Receives str or int(server id), returns list(general info of that server)'''
    log.debug(f"Attempting to get general info of server with id {server_id}")
    url = f"{API_URL}/{server_id}"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def events(server_id):
    '''Receives str or int(server id), returns list(recent server's events)'''
    log.debug(f"Attempting to get info about recent events on {server_id}")
    url = f"{API_URL}/{server_id}/events"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def kills(server_id):
    '''Receives str or int(server id), returns list(recent server's kills)'''
    log.debug(f"Attempting to get info about recent kills on {server_id}")
    url = f"{API_URL}/{server_id}/kills"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://kagstats.com/api"
get_dictionary = _config.get_dictionary

def status():
    '''Returns dictionary with info about api's stats.
    E.g total amount of players, kills and servers tracked.
    Also info about version of kagstats being used'''
    log.debug(f"Attempting to api status")
    url = f"{API}/status"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def mapstats():
    '''Returns list with known kag maps and their statistics.
    E.g name, amount of positive and negative votes, average lengh'''
    log.debug(f"Attempting to fetch mapstats")
    url = f"{API}/maps"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

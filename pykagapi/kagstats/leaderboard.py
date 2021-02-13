import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://kagstats.com/api/leaderboard"
get_dictionary = _config.get_dictionary

def global_kdr():
    '''Returns list with top 20 players across all classes of all times.
    This is based on global KDR'''
    log.debug(f"Attempting to fetch global kdr leaderboard")
    url = API_URL
    pd = get_dictionary(url)
    pydata = pd['leaderboard']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def global_kills():
    '''Returns list with top 20 players across all classes of all times.
    This is based on global amount of kills'''
    log.debug(f"Attempting to fetch global kills leaderboard")
    url = f"{API_URL}/kills"
    pd = get_dictionary(url)
    pydata = pd['leaderboard']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def global_archer():
    '''Returns list with top 20 archers of all times.
    This is based on global KDR'''
    log.debug(f"Attempting to fetch global archer leaderboard")
    url = f"{API_URL}/archer"
    pd = get_dictionary(url)
    pydata = pd['leaderboard']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def global_builder():
    '''Returns list with top 20 builders of all times.
    This is based on global KDR'''
    log.debug(f"Attempting to fetch global builder leaderboard")
    url = f"{API_URL}/builder"
    pd = get_dictionary(url)
    pydata = pd['leaderboard']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def global_knight():
    '''Returns list with top 20 knights of all times.
    This is based on global KDR'''
    log.debug(f"Attempting to fetch global knight leaderboard")
    url = f"{API_URL}/knight"
    pd = get_dictionary(url)
    pydata = pd['leaderboard']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def monthly_archer():
    '''Returns list of top 20 archers of this month.
    This is based on monthly KDR.'''
    log.debug(f"Attempting to fetch monthly archer leaderboard")
    url = f"{API_URL}/monthly/archer"
    pd = get_dictionary(url)
    pydata = pd['leaderboard']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def monthly_builder():
    '''Returns list of top 20 builders of this month.
    This is based on monthly KDR.'''
    log.debug(f"Attempting to fetch monthly builder leaderboard")
    url = f"{API_URL}/monthly/builder"
    pd = get_dictionary(url)
    pydata = pd['leaderboard']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def monthly_knight():
    '''Returns list of top 20 knights of this month.
    This is based on monthly KDR.'''
    log.debug(f"Attempting to fetch monthly knight leaderboard")
    url = f"{API_URL}/monthly/knight"
    pd = get_dictionary(url)
    pydata = pd['leaderboard']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

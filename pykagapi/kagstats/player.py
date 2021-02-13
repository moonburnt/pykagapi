import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://kagstats.com/api/players"
get_dictionary = _config.get_dictionary

def info(player_id):
    '''Receives player id as str or int.
    Returns dictionary with player's info'''
    log.debug(f"Attempting to get info about player under id {player_id}")
    url = f"{API_URL}/{player_id}"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def kills(player_id):
    '''Receives player id as str or int.
    Returns dictionary with player's recent kills'''
    log.debug(f"Attempting to get info about recent kills of {player_id}")
    url = f"{API_URL}/{player_id}/kills"
    pd = get_dictionary(url)
    pydata = pd['values']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def events(player_id):
    '''Receives player id as str or int.
    Returns list with player's recent events'''
    log.debug(f"Attempting to get info about recent events of {player_id}")
    url = f"{API_URL}/{player_id}/events"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def captures(player_id):
    '''Receives player id as str or int.
    Returns int(amount of flags captured by that player)'''
    log.debug(f"Attempting to get info about flags captured by {player_id}")
    url = f"{API_URL}/{player_id}/captures"
    pd = get_dictionary(url)
    pydata = int(pd['captures'])
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def find(player_name):
    '''Receives str(player name or part of it).
    Returns list with all matching players'''
    log.debug(f"Attempting to find players whos name match {player_name}")
    url = f"{API_URL}/search/{player_name}"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def stats_by_id(player_id):
    '''Receives player id as str or int.
    Returns dictionary with player's basic statistics.
    General info, amount of kills, flag captures - etc etc'''
    log.debug(f"Attempting to get stats of player under id {player_id}")
    url = f"{API_URL}/{player_id}/basic"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def stats_by_name(player_name):
    '''Receives str (account name of player)
    Returns dictionary with player's basic statistics.
    Basically same as stats_by_id, except via name'''
    log.debug(f"Attempting to get stats of player under name {player_name}")
    url = f"{API_URL}/lookup/{player_name}"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def top_weapons(player_id):
    '''Receives player id as str or int.
    Returns list with top of this player's weapons and amount fo kills with each'''
    #todo: get list of hitters and replace IDs with human-readable names
    log.debug(f"Attempting to get top weapons of {player_id}")
    url = f"{API_URL}/{player_id}/hitters"
    pd = get_dictionary(url)
    pydata = pd['hitters']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def nemesis(player_id):
    '''Receives player id as str or int.
    Returns dictionary with player's nemesis and amount of deaths to them'''
    log.debug(f"Attempting to get nemesis of {player_id}")
    url = f"{API_URL}/{player_id}/nemesis"
    pydata = get_dictionary(url)
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def bullied(player_id):
    '''Receives player id as str or int.
    Returns list with people whom got bullied by that player.
    Including info of each and amount of deaths to player'''
    log.debug(f"Attempting to get nemesis of {player_id}")
    url = f"{API_URL}/{player_id}/bullied"
    pd = get_dictionary(url)
    pydata = pd['bullied']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

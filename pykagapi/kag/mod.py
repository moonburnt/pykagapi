import logging
from pykagapi import _config

log = logging.getLogger(__name__)

API_URL = "https://api.kag2d.com/v1/game/thd/kag/mod"
get_dictionary = _config.get_dictionary
get_data = _config.get_data

def info(moddev, modname):
    '''Receives name of developer and name of mod.
    Returns dictionary(info about this particular mod)'''
    log.debug(f"Attempting to get information about {moddev}'s {modname} mod")
    url = f"{API_URL}/{moddev}/{modname}/info"
    pd = get_dictionary(url)
    pydata = pd['modInfo']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def files(moddev, modname):
    '''Receives name of developer and name of mod.
    Returns binary version of tar.gz archive with mod's files'''
    log.debug(f"Attempting to fetch files of {moddev}'s {modname} mod")
    url = f"{API_URL}/{moddev}/{modname}/full"
    data = get_data(url)
    log.debug(f"Successfully retrieved all files in binary form")
    return data

def server_files(moddev, modname):
    '''Receives name of developer and name of mod.
    Returns binary version of tar.gz archive with mod's server files'''
    log.debug(f"Attempting to fetch server files of {moddev}'s {modname} mod")
    url = f"{API_URL}/{moddev}/{modname}/server"
    data = get_data(url)
    log.debug(f"Successfully retrieved all files in binary form")
    return data

def client_files(moddev, modname):
    '''Receives name of developer and name of mod.
    Returns binary version of tar.gz archive with mod's client files'''
    log.debug(f"Attempting to fetch client files of {moddev}'s {modname} mod")
    url = f"{API_URL}/{moddev}/{modname}/client"
    data = get_data(url)
    log.debug(f"Successfully retrieved all files in binary form")
    return data

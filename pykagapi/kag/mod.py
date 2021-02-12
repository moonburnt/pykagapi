import requests
import json
import logging
from pykagapi import _config

log = logging.getLogger(__name__)

api_url = "https://api.kag2d.com/v1/game/thd/kag/mod"
TIMEOUT = _config.TIMEOUT
SESSION = _config.SESSION

def info(moddev, modname):
    '''Receives name of developer and name of mod, returns dictionary(info about this particular mod)'''
    log.debug(f"Attempting to get information about {moddev}'s {modname} mod")
    url = f"{api_url}/{moddev}/{modname}/info"
    data = SESSION.get(url, timeout = TIMEOUT)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['modInfo']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def files(moddev, modname):
    '''Receives name of developer and name of mod, returns mod's tar.gz archive (not as link, but as bytes. Write it into file or something)'''
    log.debug(f"Attempting to fetch files of {moddev}'s {modname} mod")
    url = f"{api_url}/{moddev}/{modname}/full"
    data = SESSION.get(url, timeout = TIMEOUT)
    data.raise_for_status()
    log.debug(f"Successfully retrieved all files in binary form")
    return data.text

def server_files(moddev, modname):
    '''Receives name of developer and name of mod, returns binary version of tar.gz archive with mod's server files'''
    log.debug(f"Attempting to fetch server files of {moddev}'s {modname} mod")
    url = f"{api_url}/{moddev}/{modname}/server"
    data = SESSION.get(url, timeout = TIMEOUT)
    data.raise_for_status()
    log.debug(f"Successfully retrieved all files in binary form")
    return data.text

def client_files(moddev, modname):
    '''Receives name of developer and name of mod, returns binary version of tar.gz archive with mod's client files'''
    log.debug(f"Attempting to fetch client files of {moddev}'s {modname} mod")
    url = f"{api_url}/{moddev}/{modname}/client"
    data = SESSION.get(url, timeout = TIMEOUT)
    data.raise_for_status()
    log.debug(f"Successfully retrieved all files in binary form")
    return data.text

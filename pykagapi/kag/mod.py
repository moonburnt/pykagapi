import requests
import json
import logging

log = logging.getLogger(__name__)

api_url = "https://api.kag2d.com/v1/game/thd/kag/mod"
timeout = 30

def info(moddev, modname):
    '''Receives name of developer and name of mod, returns dictionary(info about this particular mod)'''
    log.debug(f"Attempting to get information about {moddev}'s {modname} mod")
    url = f"{api_url}/{moddev}/{modname}/info"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    pd = json.loads(data.text)
    pydata = pd['modInfo']
    log.debug(f"Gathered following data: {pydata}")
    return pydata

def files(moddev, modname):
    '''Receives name of developer and name of mod, returns mod's tar.gz archive (not as link, but as bytes. Write it into file or something)'''
    log.debug(f"Attempting to fetch files of {moddev}'s {modname} mod")
    url = f"{api_url}/{moddev}/{modname}/full"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    log.debug(f"Successfully retrieved all files in binary form")
    return data.text

def server_files(moddev, modname):
    '''Receives name of developer and name of mod, returns binary version of tar.gz archive with mod's server files'''
    log.debug(f"Attempting to fetch server files of {moddev}'s {modname} mod")
    url = f"{api_url}/{moddev}/{modname}/server"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    log.debug(f"Successfully retrieved all files in binary form")
    return data.text

def client_files(moddev, modname):
    '''Receives name of developer and name of mod, returns binary version of tar.gz archive with mod's client files'''
    log.debug(f"Attempting to fetch client files of {moddev}'s {modname} mod")
    url = f"{api_url}/{moddev}/{modname}/client"
    data = requests.get(url, timeout = timeout)
    data.raise_for_status()
    log.debug(f"Successfully retrieved all files in binary form")
    return data.text

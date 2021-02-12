import requests
import json
import logging
from pykagapi import _config

log = logging.getLogger(__name__)

TIMEOUT = _config.TIMEOUT
SESSION = _config.SESSION

class KAGSTATS_API:
    '''Functions related to obtaining data from kagstats api hosted on https://kagstats.com/api'''
    def __init__(self):
        self.api_url = "https://kagstats.com/api"
        self.timeout = TIMEOUT
        self.session = SESSION

    def get_servers(self):
        '''Returns list of up and running servers, which get tracked by this instance of kagstats api'''
        log.debug("Attempting to get list of servers tracked by kagstats api")
        url = f"{self.api_url}/servers"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_server(self, server_id):
        '''Receives str or int(server id), returns list(general info of that server)'''
        log.debug(f"Attempting to get general info of server with id {server_id}")
        url = f"{self.api_url}/servers/{server_id}"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_server_events(self, server_id):
        '''Receives str or int(server id), returns list(info about recent server's events)'''
        log.debug(f"Attempting to get info about recent events on server with id {server_id}")
        url = f"{self.api_url}/servers/{server_id}/events"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_server_kills(self, server_id):
        '''Receives str or int(server id), returns list(info about recent server's events)'''
        log.debug(f"Attempting to get info about recent kills on server with id {server_id}")
        url = f"{self.api_url}/servers/{server_id}/kills"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_kills(self):
        '''Returns list of recent 100 kills that happend across all servers tracked by api'''
        log.debug("Attempting to get list of recent kills")
        url = f"{self.api_url}/kills"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        raw_data = json.loads(data.text)
        pydata = raw_data['values']
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_kill(self, kill_id):
        '''Receives str or int(kill id), returns dictionary with info about that kill'''
        log.debug(f"Attempting to get info about kill under id {kill_id}")
        url = f"{self.api_url}/kills/{kill_id}"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_player(self, player_id):
        '''Receives str or int(player id), returns dictionary with info about that player'''
        log.debug(f"Attempting to get info about player under id {player_id}")
        url = f"{self.api_url}/players/{player_id}"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_player_kills(self, player_id):
        '''Receives str or int(player id), returns list with info about that player's recent kills'''
        log.debug(f"Attempting to get info about recent kills of player under id {player_id}")
        url = f"{self.api_url}/players/{player_id}/kills"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        raw_data = json.loads(data.text)
        pydata = raw_data['values']
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_player_events(self, player_id):
        '''Receives str or int(player id), returns list with info about that player's recent events'''
        log.debug(f"Attempting to get info about recent events of player under id {player_id}")
        url = f"{self.api_url}/players/{player_id}/events"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def get_player_captures(self, player_id):
        '''Receives str or int(player id), returns int(amount of flags captured by that player)'''
        log.debug(f"Attempting to get info about tracked amount of flags captured by player under id {player_id}")
        url = f"{self.api_url}/players/{player_id}/captures"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        raw_data = json.loads(data.text)
        pydata = raw_data['captures']
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def find_players(self, player_name):
        '''Receives str(player name or part of it). Returns list with all matching players'''
        log.debug(f"Attempting to find players whos name match {player_name}")
        url = f"{self.api_url}/players/search/{player_name}"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def stats_by_id(self, player_id):
        '''Receives str or int(player id), returns dictionary with player's basic statistics. General info, amount of kills, flag captures - etc etc'''
        log.debug(f"Attempting to get basic statistics of player under id {player_id}")
        url = f"{self.api_url}/players/{player_id}/basic"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

    def stats_by_name(self, player_name):
        '''Receives str (account name of player), returns dictionary with player's basic statistics. Same as stats_by_id, except via name'''
        log.debug(f"Attempting to get basic statistics of player under name {player_name}")
        url = f"{self.api_url}/players/lookup/{player_name}"
        data = self.session.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        log.debug(f"Gathered following data: {pydata}")
        return pydata

if __name__ == "__main__":
    print("This is the library, its not intended to be used directly.\nCheck project's github for info about general usage:\nhttps://github.com/moonburnt/pykagapi/")

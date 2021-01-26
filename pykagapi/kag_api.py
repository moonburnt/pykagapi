import requests
import json
import logging

log = logging.getLogger(__name__)

class KAG_API:
    '''Class containing functions related to obtaining data from official api of King Arthur's Gold hosted on https://api.kag2d.com/v1'''
    def __init__(self):
        #API url
        self.api_url = "https://api.kag2d.com/v1"
        #default timeout for requests
        self.timeout = 30

    def get_api_info(self):
        '''Returns dictionary with general info about this api'''
        data = requests.get(self.api_url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata

    def get_game_info(self):
        '''Returns dictionary with general info about KAG'''
        url = f"{self.api_url}/game/thd/kag"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['gameInfo']

    #Player shenanigans
    def get_player_overall_info(self, nickname):
        '''Receives player's nickname (str), returns dictionary with player's overall info'''
        url = f"{self.api_url}/player/{nickname}"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata

    def get_player_info(self, nickname):
        '''Receives player's nickname (str), returns dictionary with player's general info'''
        url = f"{self.api_url}/player/{nickname}/info"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['playerInfo']

    def get_player_status(self, nickname):
        '''Receives player's nickname (str), returns dictionary with player's status'''
        url = f"{self.api_url}/player/{nickname}/status"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['playerStatus']

    def get_player_banflags(self, nickname):
        '''Receives player's nickname (str), returns dictionary with player's banflags'''
        url = f"{self.api_url}/player/{nickname}/banflags"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['playerBanFlags']

    def get_player_private_info(self, login, password, nickname=None):
        '''Receives your (unless you are admin) login, password, nickname (strs), returns dictionary with private info'''
        if not nickname:
            nickname = login
        url = f"{self.api_url}/player/{nickname}/myinfo"
        data = requests.get(url, auth=(login, password), timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['playerInfoPrivate']

    def get_player_private_forum_info(self, login, password, nickname=None):
        '''Receives your (unless you are admin) login, password, nickname (strs), returns dictionary with private forum info'''
        if not nickname:
            nickname = login
        url = f"{self.api_url}/player/{nickname}/foruminfo"
        data = requests.get(url, auth=(login, password), timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['playerInfoForum']

    def get_player_avatar(self, nickname, size="m"):
        '''Receives player's nickname and avatar size ("s", "m" or "l") (all strs), returns str link to pfp of that size'''
        url = f"{self.api_url}/player/{nickname}/avatar/{size}"
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return str(list(pydata.values())[0])

    def get_player_avatars(self, nickname):
        '''Receives str(nickname), returns dictionary with links to large, medium and small pfps'''
        url = f"{self.api_url}/player/{nickname}/avatar/"
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata

    #Token shenanigans
    def get_token(self, login, password):
        '''Receives player's login and password (str), returns player's authentication token (str)'''
        url = f"{self.api_url}/player/{login}/token/new"
        data = requests.get(url, auth=(login, password), timeout = self.timeout)
        pydata = json.loads(data.text)
        return str(pydata['playerToken'])

    def verify_token(self, username, token):
        #'''Receives username and token. Verifies if token is valid for that person. Returns True if its valid or False otherwise'''
        '''Receives username and token. Verifies if token is valid for that person. Returns True if its valid'''
        url = f"{self.api_url}/player/{username}/token/{token}"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        #status = data.status_code
        #if status == 200:
        #    return True
        #else:
        #    return False
        return True

    def get_ip(self):
        '''Receive your IP (str) from kag api'''
        url = f"{self.api_url}/myip"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return str(pydata['yourIP'])

    def get_filters(self):
        '''Receive dic(info) with valid filters used in server-related requests'''
        url = f"{self.api_url}/game/1/servers/filterinfo"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['serverListFilterFields']

    def get_servers(self, filters=None):
        '''Optionally receives list(filters). Returns list with matching servers (or all known servers, if used without filter). May take a while to process'''
        if filters:
            jfilters = json.dumps(filters)
            #url = self.api_url+'/game/1/servers?filters='+jfilters
            url = f"{self.api_url}/game/1/servers?filters={jfilters}"
        else:
            url = f"{self.api_url}/game/1/servers"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['serverList']

    def get_alive_servers(self):
        '''Returns list with servers thats up and running. Or at least according to api'''
        filters = [{'field': 'current', 'op': 'eq', 'value': True}]
        pydata = self.get_servers(filters)
        return pydata

    def get_active_servers(self):
        '''Returns list with servers that contain players'''
        filters = [{'field': 'current', 'op': 'eq', 'value': True}, {'field': 'currentPlayers', 'op': 'ge', 'value': 1}]
        pydata = self.get_servers(filters)
        return pydata

    def get_server_status(self, ip, port):
        '''Receives str(ip) and int(port), returns dictionary with server's info'''
        url = f"{self.api_url}/game/thd/kag/server/{ip}/{port}/status"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['serverStatus']

    def get_server_minimap(self, ip, port):
        '''Receives str(ip) and int(port), returns server's current map image in binary form (use something like Pillow+BytesIO to decode it)'''
        url = f"{self.api_url}/game/thd/kag/server/{ip}/{port}/minimap"
        data = requests.get(url, timeout = self.timeout)
        return data.content

    def get_mod_info(self, moddev, modname):
        '''Receives str(name of developer) and str(name of mod), returns dictionary(info about this particular mod)'''
        url = f"{self.api_url}/game/thd/kag/mod/{moddev}/{modname}/info"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['modInfo']

    def get_mod(self, moddev, modname):
        '''Receives str(name of developer) and str(name of mod), returns mod's tar.gz archive (not as link, but as bytes. Write it into file or something)'''
        url = f"{self.api_url}/game/thd/kag/mod/{moddev}/{modname}/full"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        return data.text

    def get_mod_server(self, moddev, modname):
        '''Receives str(name of developer) and str(name of mod), returns tar.gz archive with mod's server files'''
        url = f"{self.api_url}/game/thd/kag/mod/{moddev}/{modname}/server"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        return data.text

    def get_mod_client(self, moddev, modname):
        '''Receives str(name of developer) and str(name of mod), returns tar.gz archive with mod's client files'''
        url = f"{self.api_url}/game/thd/kag/mod/{moddev}/{modname}/client"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        return data.text

    def get_mod_list(self, filters = None):
        '''Optionally receives list(filters), returns list with matching (or all, if nothing has been passed) registered mods (but nobody bothers to do that anymore, so its not that long)'''
        if filters:
            jfilters = json.dumps(filters)
            #url = self.api_url+'/game/thd/kag/mods?filters='+jfilters
            url = f"{self.api_url}/game/thd/kag/mods?filters={jfilters}"
        else:
            url = f"{self.api_url}/game/thd/kag/mods"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['modList']

    def get_mod_filters(self):
        '''Returns list of valid filters to be used with get_mod_list()'''
        url = f"{self.api_url}/game/thd/kag/mods/filterinfo"
        data = requests.get(url, timeout = self.timeout)
        data.raise_for_status()
        pydata = json.loads(data.text)
        return pydata['modListFilterFields']

if __name__ == "__main__":
    print("This is the library, its not intended to be used directly.\nCheck project's wiki for info about general usage:\nhttps://github.com/moonburnt/pykagapi/wiki")

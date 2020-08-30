## Python bindings for official kag api. Was made to serve as library, but feel free to use it as reference or whatever
import requests
import json

class KAG_API:
    '''Class containing functions related to obtaining data from official api of King Arthur's Gold'''
    def __init__(self):
        #API url
        self.siteurl = "https://api.kag2d.com/v1"
        #default timeout for requests
        self.timeout = 30

    def get_api_info(self):
        '''Returns dictionary with general info about this api'''
        data = requests.get(self.siteurl, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata

    def get_game_info(self):
        '''Returns dictionary with general info about KAG'''
        url = "{}/game/thd/kag".format(self.siteurl)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['gameInfo']

    #Player shenanigans
    def get_player_overall_info(self, nickname):
        '''Receives player's nickname (str), returns dictionary with player's overall info'''
        url = "{}/player/{}".format(self.siteurl, nickname)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata

    def get_player_info(self, nickname):
        '''Receives player's nickname (str), returns dictionary with player's general info'''
        url = "{}/player/{}/info".format(self.siteurl, nickname)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['playerInfo']

    def get_player_status(self, nickname):
        '''Receives player's nickname (str), returns dictionary with player's status'''
        url = "{}/player/{}/status".format(self.siteurl, nickname)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['playerStatus']

    def get_player_banflags(self, nickname):
        '''Receives player's nickname (str), returns dictionary with player's banflags'''
        url = "{}/player/{}/banflags".format(self.siteurl, nickname)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['playerBanFlags']

    def get_player_private_info(self, login, password, nickname=None):
        '''Receives your (unless you are admin) login, password, nickname (strs), returns dictionary with private info'''
        #TODO: add ability to authorize with token, if possible. Same for private forum below
        if not nickname:
            nickname = login
        url = "{}/player/{}/myinfo".format(self.siteurl, nickname)
        data = requests.get(url, auth=(login, password), timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['playerInfoPrivate']

    def get_player_private_forum_info(self, login, password, nickname=None):
        '''Receives your (unless you are admin) login, password, nickname (strs), returns dictionary with private forum info'''
        if not nickname:
            nickname = login
        url = "{}/player/{}/foruminfo".format(self.siteurl, nickname)
        data = requests.get(url, auth=(login, password), timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['playerInfoForum']

    def get_player_avatar(self, nickname, size="m"):
        '''Receives player's nickname and avatar size ("s", "m" or "l") (all strs), returns str link to pfp of that size'''
        url = "{}/player/{}/avatar/{}".format(self.siteurl, nickname, size)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return str(list(pydata.values())[0])

    def get_player_avatars(self, nickname):
        '''Receives str(nickname), returns dictionary with links to large, medium and small pfps'''
        url = "{}/player/{}/avatar/".format(self.siteurl, nickname)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata

    #Token shenanigans
    def get_token(self, login, password):
        '''Receives player's login and password (str), returns player's authentication token (str)'''
        url = "{}/player/{}/token/new".format(self.siteurl, login)
        data = requests.get(url, auth=(login, password), timeout = self.timeout)
        pydata = json.loads(data.text)
        return str(pydata['playerToken'])

    def verify_token(self, username, token):
        '''Receives username and token. Verifies if token is valid for that person. Returns True if its valid or False otherwise'''
        url = "{}/player/{}/token/{}".format(self.siteurl, username, token)
        data = requests.get(url, timeout = self.timeout)
        status = data.status_code
        if status == 200:
            return True
        else:
            return False

    def get_ip(self):
        '''Receive your IP (str) from kag api'''
        url = "{}/myip".format(self.siteurl)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return str(pydata['yourIP'])

    def get_filters(self):
        '''Receive dic(info) with valid filters used in server-related requests'''
        url = "{}/game/1/servers/filterinfo".format(self.siteurl)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['serverListFilterFields']

    def get_servers(self, filters=None):
        '''Optionally receives list(filters). Returns list with matching servers (or all known servers, if used without filter). May take a while to process'''
        if filters:
            jfilters = json.dumps(filters)
            url = self.siteurl+'/game/1/servers?filters='+jfilters
        else:
            url = "{}/game/1/servers".format(self.siteurl)
        data = requests.get(url, timeout = self.timeout)
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
        url = "{}/game/thd/kag/server/{}/{}/status".format(self.siteurl, ip, port)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['serverStatus']

    def get_server_minimap(self, ip, port):
        '''Receives str(ip) and int(port), returns server's current map image in binary form (use something like Pillow+BytesIO to decode it)'''
        url = "{}/game/thd/kag/server/{}/{}/minimap".format(self.siteurl, ip, port)
        data = requests.get(url, timeout = self.timeout)
        return data.content

    def get_mod_info(self, moddev, modname):
        '''Receives str(name of developer) and str(name of mod), returns dictionary(info about this particular mod)'''
        url = "{}/game/thd/kag/mod/{}/{}/info".format(self.siteurl, moddev, modname)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['modInfo']

    def get_mod(self, moddev, modname):
        '''Receives str(name of developer) and str(name of mod), returns mod's tar.gz archive (not as link, but as bytes. Write it into file or something)'''
        url = "{}/game/thd/kag/mod/{}/{}/full".format(self.siteurl, moddev, modname)
        data = requests.get(url, timeout = self.timeout)
        return data.text

    def get_mod_server(self, moddev, modname):
        '''Receives str(name of developer) and str(name of mod), returns tar.gz archive with mod's server files'''
        url = "{}/game/thd/kag/mod/{}/{}/server".format(self.siteurl, moddev, modname)
        data = requests.get(url, timeout = self.timeout)
        return data.text

    def get_mod_client(self, moddev, modname):
        '''Receives str(name of developer) and str(name of mod), returns tar.gz archive with mod's client files'''
        url = "{}/game/thd/kag/mod/{}/{}/client".format(self.siteurl, moddev, modname)
        data = requests.get(url, timeout = self.timeout)
        return data.text

    def get_mod_list(self, filters = None):
        '''Optionally receives list(filters), returns list with matching (or all, if nothing has been passed) registered mods (but nobody bothers to do that anymore, so its not that long)'''
        if filters:
            jfilters = json.dumps(filters)
            url = self.siteurl+'/game/thd/kag/mods?filters='+jfilters
        else:
            url = "{}/game/thd/kag/mods".format(self.siteurl)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['modList']

    def get_mod_filters(self):
        '''Returns list of valid filters to be used with get_mod_list()'''
        url = "{}/game/thd/kag/mods/filterinfo".format(self.siteurl)
        data = requests.get(url, timeout = self.timeout)
        pydata = json.loads(data.text)
        return pydata['modListFilterFields']

if __name__ == "__main__":
    print("This is the library, its not intended to be used directly.\nCheck project's wiki for info about general usage:\nhttps://github.com/moonburnt/pykagapi/wiki")

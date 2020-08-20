*I dont know why it exists*

**Description:**

Well, long story short - its python bindings (or something like that) to kag's official api (may add support for [kagstats api](https://github.com/Harrison-Miller/kagstats) later). Import it as library into your code, call some function - get info you've been seeking for. No knowledge of networking libraries required required.

**Example Usage:**

Getting the list of servers with players on them:

`import pykagapi

api = pykagapi.KAG_API()
servers = api.get_active_servers()
print(servers)`

**Unimplemented features**:

- [Devgroups](https://developers.thd.vg/api/devgroups.html), because I dont have access to these to check if these are working
- [Put server status](https://developers.thd.vg/api/servers.html#put--game-(gamedev)-(game)-server-(ip)-(int-port)-status) and [put minimap](https://developers.thd.vg/api/servers.html#put--game-(gamedev)-(game)-server-(ip)-(int-port)-minimap) - for same reasons
- [Mods stuff](https://developers.thd.vg/api/mods.html), because nobody bothers to register mods anymore
- /terms/status and /receiveemails/status from [players](https://developers.thd.vg/api/players.html) - these seem to be broken
- "start" and "limit" for server info requests

**TODO**:

- Remove obsolete comments from debug era
- Make descriptions of functions better

**LICENSE**:

[WTFPL](LICENSE)

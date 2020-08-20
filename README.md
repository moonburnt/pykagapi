*I dont know why it exists*

**Description:**

Well, long story short - its python bindings (or something like that) to official api of King Arhur's Gold (may add support for [kagstats api](https://github.com/Harrison-Miller/kagstats) later). Import it as library into your code, call some function - get info you've been seeking for. No knowledge of networking libraries required.

**Dependencies:**

- python 3.7+ (may work on previous versions, didnt test)
- python-requests

**Example Usage:**

Getting game's description:
```python
import pykagapi

api = pykagapi.KAG_API()
gameinfo = api.get_game_info()
description = gameinfo['description']
print(description)
```

Output:

`KAG is a 2D cooperative war game played with up to 32 players. Play as Knight, Archer or Builder in a large medieval world with physics allowing the construction (and destruction!) of medieval fortresses.`

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

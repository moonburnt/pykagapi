*I dont know why it exists*

**Description:**

Well, long story short - its python wrapper (or something like that) to official api of King Arhur's Gold (may add support for [kagstats api](https://github.com/Harrison-Miller/kagstats) later). Import it as library into your code, call some function - get info you've been seeking for. No knowledge of networking libraries required. Or, well, use it as reference while writing your own code - WTFPL license is equal to public domain, meaning Im perfectly fine with other people copypasting parts of this lib

**Dependencies:**

- python 3.7+ (may work on previous versions, didnt test)
- python-requests

**Example Usage:**

Getting amount of active servers:
```python
import pykagapi

api = pykagapi.KAG_API()
servers = api.get_active_servers()
print("There are currently {} servers with players on them!".format(len(servers)))
```

Example output:

`There are currently 6 servers with players on them!`

**Unimplemented features**:

- Everything that isnt "get" requests, because Im just a regular player and dont have ability to upload or remove anything (most of [devgroups](https://developers.thd.vg/api/devgroups.html), [put server status](https://developers.thd.vg/api/servers.html#put--game-(gamedev)-(game)-server-(ip)-(int-port)-status) and [put minimap](https://developers.thd.vg/api/servers.html#put--game-(gamedev)-(game)-server-(ip)-(int-port)-minimap), few entries from [mods stuff](https://developers.thd.vg/api/mods.html) used to upload mods and verify them)
- /terms/status and /receiveemails/status from [players](https://developers.thd.vg/api/players.html) - these seem to be broken
- "start" and "limit" for server info requests

**TODO**:

- Remove obsolete comments from debug era
- Make descriptions of functions better

**LICENSE**:

[WTFPL](LICENSE)

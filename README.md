*I dont know why it exists*

# Description:

Well, long story short - its python wrapper (or something like that) to King Arthurs Gold-related apis (currently has nearly full support of [official kag api](https://api.kag2d.com/v1) and partial support of [kagstats api](https://kagstats.com/api). Import it as library into your code, call some function - get info you've been seeking for. No knowledge of networking libraries required. Or, well, use it as reference while writing your own code - [WTFPL license](LICENSE) is equal to public domain, meaning Im perfectly fine with other people copypasting parts of this lib into their projects

# Dependencies:

- python 3.7+ (may work on previous versions, didnt test)
- python-requests

# Example Usage:

## Getting amount of active servers:
```python
from pykagapi import kag_api

api = kag_api.KAG_API()
servers = api.get_active_servers()
servers_amount = len(servers)
print(f"There are currently {servers_amount} servers that have players on them!")
```

## Example output:

`There are currently 6 servers with players on them!`

# Currently unimplemented api calls:

## Kag api:

- Everything that isnt "get" requests, because Im just a regular player and dont have ability to upload or remove anything (most of [devgroups](https://developers.thd.vg/api/devgroups.html), [put server status](https://developers.thd.vg/api/servers.html#put--game-(gamedev)-(game)-server-(ip)-(int-port)-status) and [put minimap](https://developers.thd.vg/api/servers.html#put--game-(gamedev)-(game)-server-(ip)-(int-port)-minimap), few entries from [mods stuff](https://developers.thd.vg/api/mods.html) used to upload mods and verify them)
- /terms/status and /receiveemails/status from [players](https://developers.thd.vg/api/players.html) - these seem to be broken
- "start" and "limit" for server info requests

## Kagstats api:

The only **implemented** part right now is content of [general api's source](https://github.com/Harrison-Miller/kagstats/blob/master/api/api.go). With the exclusion of following:
- /players (without arguments), coz I didnt find use for it
- /players/{id}/refresh - coz it doesnt seem to be any usefull

As for the rest - soon™

# LICENSE:

[WTFPL](LICENSE)

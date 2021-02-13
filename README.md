*I dont know why it exists*

# pykagapi

## Description:

Well, long story short - its python wrapper (or something like that) for King Arthurs Gold-related apis - [kag api v1](https://api.kag2d.com/v1) and [kagstats api](https://kagstats.com/api). Import it as library into your code, call some function - get info you've been seeking for. No knowledge of networking libraries required. Or, well, use it as reference while writing your own code - [WTFPL license](LICENSE) is equal to public domain, meaning Im perfectly fine with other people copypasting parts of this lib into their projects

## Dependencies:

- python 3.8 (may work on previous versions, didnt test)
- python-requests

## Example Usage:

### Getting amount of active servers:
```python
from pykagapi import kag

servers = kag.servers.active()
servers_amount = len(servers)
print(f"There are currently {servers_amount} servers that have players on them!")
```

### Example output:

`There are currently 6 servers with players on them!`

## Currently unimplemented api calls:

### KAG API:

- Everything that isnt "get" requests, because Im just a regular player and dont have ability to upload or remove anything
- "start" and "limit" for server info requests

### KAGSTATS API:

- `https://kagstats.com/api/players`, because there are few thousand players known to database. Do you really need to get them all?
- `https://kagstats.com/api/players/{id}/refresh`, because it doesnt seem to do anything
- Whatever I didnt notice while casually reading [api's source codes](https://github.com/Harrison-Miller/kagstats/tree/master/api)

## LICENSE:

[WTFPL](LICENSE)

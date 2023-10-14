# pykagapi

## Description:

*pykagapi* - is a python wrapper for King Arthurs Gold-related apis ([kag api v1](https://api.kag2d.com/v1) and [kagstats api](https://kagstats.com/api)).
Use it as you please.

## Dependencies:

- python 3.10 (may work on previous versions, didnt test)
- requests

## Example Usage:

### Getting general api info:

```python
from pykagapi import kag

with kag.get_client() as c:
    print(c.get_api_info())
```

### Getting amount of currently active servers:

```python
from pykagapi import kag

with kag.get_client() as c:
    servers_amount = len(kag.extra.get_active_servers()["serverList"])

print(f"There are currently {servers_amount} servers with players!")
```

Example output:
`There are currently 6 servers with players!`


## Currently unimplemented api calls:

### KAG API:

- Everything that isn't "get" requests, because Im just a regular player and dont have ability to upload or remove anything

### KAGSTATS API:

- `https://kagstats.com/api/players`, because there are few thousand players known to database. Do you really need to get them all?
- `https://kagstats.com/api/players/{id}/refresh`, because it doesnt seem to do anything
- Whatever I didnt notice while casually reading [api's source codes](https://github.com/Harrison-Miller/kagstats/tree/master/api)


## TODO:

- Support for non-GET requests
- Async clients
- Automated tests

## LICENSE:

[WTFPL](LICENSE)

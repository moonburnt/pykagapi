# pykagapi

## Description:

*pykagapi* - a python wrapper for King Arthurs Gold-related APIs ([KAG API v1](https://api.kag2d.com/v1) and [KAG Stats API](https://kagstats.com/api)).
Use it as you please, feel free to contribute!

## Dependencies:

- python 3.10+
- requests
- aiohttp (for async client)

## Installation:

### From source:

- Install [poetry](https://python-poetry.org/docs/#installation)
- Clone this repo: `git clone https://github.com/moonburnt/pykagapi.git`
- Enter project's directory: `cd pykagapi`
- `poetry install`

### From pypi:

- `pip install pykagapi`

## Example Usage:

### Getting general api info:

```python
from pykagapi import kag

with kag.get_client() as c:
    print(c.get_api_info())
```

### Getting general api info asynchroniously:

```python
from pykagapi import kag
import asyncio

async def main():
    async with kag.get_async_client() as c:
        print(await c.get_api_info())

asyncio.run(main())
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

- `https://kagstats.com/api/players/{id}/refresh`, because it doesnt seem to do anything
- Whatever I didnt notice while casually reading [api's source codes](https://github.com/Harrison-Miller/kagstats/tree/master/api)


## TODO:

- Support for non-GET requests
- Automated tests
- Support for "limit"/"start" in list views of kagstats api
- Make async client optional

## LICENSE:

[MIT](LICENSE)

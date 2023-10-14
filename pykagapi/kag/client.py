from json import dumps
from typing import Optional, Tuple, List, Dict, Literal
from pykagapi.core.client import APIClient


class KagAPIClient(APIClient):
    def __init__(self, timeout: Optional[int] = None):
        super().__init__(timeout=timeout, api_root="https://api.kag2d.com/v1")

        self.base_endpoints = self.base_endpoints | {
            "mod": f"{self.api_root}/game/thd/kag/mod",
            "mods": f"{self.api_root}/game/thd/kag/mods",
            "player": f"{self.api_root}/player",
            "server": f"{self.api_root}/game/thd/kag/server",
            "servers": f"{self.api_root}/game/1/servers",
        }

    def get_api_info(self) -> dict:
        """Get general info about this api."""

        return self._get(self.base_endpoints["root"]).json()

    def get_game_info(self) -> dict:
        """Get general info about this game."""

        return self._get(f"{self.base_endpoints['root']}/game/thd/kag").json()

    def get_my_ip(self) -> dict:
        """Get your IP as seen by KAG API."""

        return self._get(f"{self.base_endpoints['root']}/myip").json()

    def get_mod_info(self, author: str, mod: str) -> dict:
        """Get info about requested mod."""

        return self._get(
            f"{self.base_endpoints['mod']}/{author}/{mod}/info"
        ).json()

    def get_mod_files(self, author: str, mod: str) -> bytes:
        """Get requested mod's files."""

        return self._get(
            f"{self.base_endpoints['mod']}/{author}/{mod}/full"
        ).content

    def get_mod_client_files(self, author: str, mod: str) -> bytes:
        """Get requested mod's client files."""

        return self._get(
            f"{self.base_endpoints['mod']}/{author}/{mod}/client"
        ).content

    def get_mod_server_files(self, author: str, mod: str) -> bytes:
        """Get requested mod's server files."""

        return self._get(
            f"{self.base_endpoints['mod']}/{author}/{mod}/server"
        ).content

    def get_mods(
        self,
        filters: Optional[List[Dict[str, str]]] = None,
        limit: Optional[int] = None,
        start: Optional[int] = None,
    ) -> dict:
        """Get registered mods."""

        params = {}
        if filters:
            params["filters"] = dumps(filters)

        if limit:
            params["limit"] = limit

        if start:
            params["start"] = start

        return self._get(self.base_endpoints["mods"], params=params).json()

    def get_mods_filterinfo(self) -> dict:
        """Get optional filters to use with 'get_mods()' request."""

        return self._get(f"{self.base_endpoints['mods']}/filterinfo").json()

    def get_player(self, player: str) -> dict:
        """Get full player's info."""

        return self._get(f"{self.base_endpoints['player']}/{player}").json()

    def get_player_info(self, player: str) -> dict:
        """Get player's general info."""

        return self._get(
            f"{self.base_endpoints['player']}/{player}/info"
        ).json()

    def get_player_status(self, player: str) -> dict:
        """Get player's status."""

        return self._get(
            f"{self.base_endpoints['player']}/{player}/status"
        ).json()

    def get_player_banflags(self, player: str) -> dict:
        """Get player's banflags."""

        return self._get(
            f"{self.base_endpoints['player']}/{player}/bandflags"
        ).json()

    def get_player_myinfo(self, login: str, password: str) -> dict:
        """Get your own private info."""

        return self._get(
            url=f"{self.base_endpoints['player']}/{player}/myinfo",
            auth=(login, password),
        ).json()

    def get_player_foruminfo(self, login: str, password: str) -> dict:
        """Get your own forum info."""

        return self._get(
            url=f"{self.base_endpoints['player']}/{player}/foruminfo",
            auth=(login, password),
        ).json()

    def get_player_avatar(
        self, player: str, size: Optional[Literal["s", "m", "l"]] = None
    ) -> dict:
        """Get player's forum avatar."""

        url = f"{self.base_endpoints['player']}/{player}/avatar"
        if size:
            url += f"/{size}"

        return self._get(url).json()

    def get_player_token(self, login: str, password: str) -> dict:
        """Get your auth token."""

        return self._get(
            url=f"{self.base_endpoints['player']}/{login}/token/new",
            auth=(login, password),
        ).json()

    def get_player_token_validation(self, user: str, token: str) -> bool:
        """Verify if provided token is valid for requested user."""

        resp = self._get(
            url=f"{self.base_endpoints['player']}/{user}/token/{token}",
            auth=(login, password),
            validate_status=False,
        )

        if resp.status_code == 200:
            return True
        elif resp.status_code == 404:
            return False
        else:
            resp.raise_for_status()

    def get_server_status(self, ip: str, port: int) -> dict:
        """Get server info."""

        return self._get(
            f"{self.base_endpoints['server']}/{ip}/{port}/status"
        ).json()

    def get_server_minimap(self, ip: str, port: int) -> bytes:
        """Get server's current minimap state.

        Use something like pillow + BytesIO to decode it.
        """

        return self._get(
            f"{self.base_endpoints['server']}/{ip}/{port}/minimap"
        ).content

    def get_servers_filterinfo(self) -> dict:
        """Get optional filters to use with 'get_servers()' request."""

        return self._get(f"{self.base_endpoints['servers']}/filterinfo").json()

    def get_servers(
        self,
        filters: Optional[List[Dict[str, str]]] = None,
        limit: Optional[int] = None,
        start: Optional[int] = None,
    ) -> dict:
        """Get all servers known to api.

        Without any filters or limits, may take a while.
        """

        params = {}
        if filters:
            params["filters"] = dumps(filters)

        if limit:
            params["limit"] = limit

        if start:
            params["start"] = start

        return self._get(self.base_endpoints["servers"], params=params).json()

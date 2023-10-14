from typing import Optional, Tuple, List, Dict, Literal
from pykagapi.core.async_client import AsyncAPIClient


class AsyncKagStatsAPIClient(AsyncAPIClient):
    def __init__(
        self,
        timeout: Optional[int] = None,
        api_root: str = "https://kagstats.com/api",
    ):
        super().__init__(timeout=timeout, api_root=api_root)

        self.base_endpoints = self.base_endpoints | {
            "kills": f"{self.api_root}/kills",
            "leaderboard": f"{self.api_root}/leaderboard",
            "players": f"{self.api_root}/players",
            "servers": f"{self.api_root}/servers",
        }

    # TODO: pagination support
    async def get_kills(self) -> dict:
        """Get recent 100 kills from API."""

        resp = await self._get(self.base_endpoints["kills"])

        return await resp.json()

    # Broken on the api-side
    # async def get_kills_info(self, kill_id: int) -> dict:
    #     """Get info about specific kill."""

    #     resp = await self._get(f"{self.base_endpoints['kills']}/{kill_id}")

    #     return await resp.json()

    async def get_leaderboard(self) -> dict:
        """Get top-20 players based on their overall KDR."""

        resp = await self._get(self.base_endpoints["leaderboard"])

        return await resp.json()

    async def get_leaderboard_kills(self) -> dict:
        """Get top-20 players based on their overall kills amount."""

        resp = await self._get(f"{self.base_endpoints['leaderboard']}/kills")

        return await resp.json()

    async def get_leaderboard_archer(self) -> dict:
        """Get top-20 archers based on their overall KDR."""

        resp = await self._get(f"{self.base_endpoints['leaderboard']}/archer")

        return await resp.json()

    async def get_leaderboard_builder(self) -> dict:
        """Get top-20 builders based on their overall KDR."""

        resp = await self._get(f"{self.base_endpoints['leaderboard']}/builder")

        return await resp.json()

    async def get_leaderboard_knight(self) -> dict:
        """Get top-20 knights based on their overall KDR."""

        resp = await self._get(f"{self.base_endpoints['leaderboard']}/knight")

        return await resp.json()

    async def get_leaderboard_monthly_archer(self) -> dict:
        """Get top-20 archers based on their KDR this month."""

        resp = await self._get(
            f"{self.base_endpoints['leaderboard']}/monthly/archer"
        )

        return await resp.json()

    async def get_leaderboard_monthly_builder(self) -> dict:
        """Get top-20 builders based on their KDR this month."""

        resp = await self._get(
            f"{self.base_endpoints['leaderboard']}/monthly/builder"
        )

        return await resp.json()

    async def get_leaderboard_monthly_knight(self) -> dict:
        """Get top-20 knights based on their KDR this month."""

        resp = await self._get(
            f"{self.base_endpoints['leaderboard']}/monthly/knight"
        )

        return await resp.json()

    async def get_players(self) -> dict:
        """Get list of players known to API.
        May take a while.
        """

        resp = await self._get(self.base_endpoints["players"])

        return await resp.json()

    async def get_players_info(self, player_id: int) -> dict:
        """Get player info."""

        resp = await self._get(f"{self.base_endpoints['players']}/{player_id}")

        return await resp.json()

    async def get_players_kills(self, player_id: int) -> dict:
        """Get player's recent kills."""

        resp = await self._get(
            f"{self.base_endpoints['players']}/{player_id}/kills"
        )

        return await resp.json()

    # async def get_players_events(self, player_id: int) -> dict:
    #     """Get player's recent events."""

    #     resp = await self._get(
    #         f"{self.base_endpoints['players']}/{player_id}/events"
    #     )

    #     return await resp.json()

    async def get_players_captures(self, player_id: int) -> dict:
        """Get player's flag captures."""

        resp = await self._get(
            f"{self.base_endpoints['players']}/{player_id}/captures"
        )

        return await resp.json()

    async def get_players_lookup(self, username: str) -> dict:
        """Find players matching provided name (or part of it)"""

        resp = await self._get(
            f"{self.base_endpoints['players']}/search/{username}"
        )

        return await resp.json()

    async def get_players_stats_by_id(self, player_id: int) -> dict:
        """Get player's stats by id."""

        resp = await self._get(
            f"{self.base_endpoints['players']}/{player_id}/basic"
        )

        return await resp.json()

    async def get_players_stats_by_username(self, player_name: int) -> dict:
        """Get player's stats by username."""

        resp = await self._get(
            f"{self.base_endpoints['players']}/lookup/{player_name}"
        )

        return await resp.json()

    async def get_players_hitters(self, player_id: int) -> dict:
        """Get favorite player's weapons and related stats."""

        resp = await self._get(
            f"{self.base_endpoints['players']}/{player_id}/hitters"
        )

        return await resp.json()

    async def get_players_nemesis(self, player_id: int) -> dict:
        """Get whom killed this player the most."""

        resp = await self._get(
            f"{self.base_endpoints['players']}/{player_id}/nemesis"
        )

        return await resp.json()

    async def get_players_bullied(self, player_id: int) -> dict:
        """Get whos been killed by this player the most."""

        resp = await self._get(
            f"{self.base_endpoints['players']}/{player_id}/bullied"
        )

        return await resp.json()

    async def get_status(self) -> dict:
        """Get overview of this API endpoint."""

        resp = await self._get(f"{self.base_endpoints['root']}/status")

        return await resp.json()

    async def get_maps(self) -> dict:
        """Get map-related statistics."""

        resp = await self._get(f"{self.base_endpoints['root']}/maps")

        return await resp.json()

    async def get_maps(self) -> dict:
        """Get map-related statistics."""

        resp = await self._get(f"{self.base_endpoints['root']}/maps")

        return await resp.json()

    async def get_servers(self) -> dict:
        """Get active servers."""

        resp = await self._get(self.base_endpoints["servers"])

        return await resp.json()

    async def get_servers_info(self, server_id: int) -> dict:
        """Get detailed info of the selected server."""

        resp = await self._get(f"{self.base_endpoints['servers']}/{server_id}")

        return await resp.json()

    # async def get_servers_events(self, server_id: int) -> dict:
    #     """Get recent server's events."""

    #     resp = await self._get(
    #         f"{self.base_endpoints['servers']}/{server_id}/events"
    #     )

    #     return await resp.json()

    # async def get_servers_kills(self, server_id: int) -> dict:
    #     """Get recent server's kills."""

    #     resp = await self._get(
    #         f"{self.base_endpoints['servers']}/{server_id}/kills"
    #     )

    #     return await resp.json()

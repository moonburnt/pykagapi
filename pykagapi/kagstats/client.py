from typing import Optional, Tuple, List, Dict, Literal
from pykagapi.core.client import APIClient


class KagStatsAPIClient(APIClient):
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
    def get_kills(self) -> dict:
        """Get recent 100 kills from API."""

        return self._get(self.base_endpoints["kills"]).json()

    # Seemingly broken: https://github.com/Harrison-Miller/kagstats/issues/50
    # def get_kills_info(self, kill_id: int) -> dict:
    #     """Get info about specific kill."""

    #     return self._get(f"{self.base_endpoints['kills']}/{kill_id}").json()

    def get_leaderboard(self) -> dict:
        """Get top-20 players based on their overall KDR."""

        return self._get(self.base_endpoints["leaderboard"]).json()

    def get_leaderboard_kills(self) -> dict:
        """Get top-20 players based on their overall kills amount."""

        return self._get(f"{self.base_endpoints['leaderboard']}/kills").json()

    def get_leaderboard_archer(self) -> dict:
        """Get top-20 archers based on their overall KDR."""

        return self._get(f"{self.base_endpoints['leaderboard']}/archer").json()

    def get_leaderboard_builder(self) -> dict:
        """Get top-20 builders based on their overall KDR."""

        return self._get(f"{self.base_endpoints['leaderboard']}/builder").json()

    def get_leaderboard_knight(self) -> dict:
        """Get top-20 knights based on their overall KDR."""

        return self._get(f"{self.base_endpoints['leaderboard']}/knight").json()

    def get_leaderboard_monthly_archer(self) -> dict:
        """Get top-20 archers based on their KDR this month."""

        return self._get(
            f"{self.base_endpoints['leaderboard']}/monthly/archer"
        ).json()

    def get_leaderboard_monthly_builder(self) -> dict:
        """Get top-20 builders based on their KDR this month."""

        return self._get(
            f"{self.base_endpoints['leaderboard']}/monthly/builder"
        ).json()

    def get_leaderboard_monthly_knight(self) -> dict:
        """Get top-20 knights based on their KDR this month."""

        return self._get(
            f"{self.base_endpoints['leaderboard']}/monthly/knight"
        ).json()

    def get_players(self) -> dict:
        """Get list of players known to API.
        May take a while.
        """

        return self._get(self.base_endpoints["players"]).json()

    def get_players_info(self, player_id: int) -> dict:
        """Get player info."""

        return self._get(f"{self.base_endpoints['players']}/{player_id}").json()

    def get_players_kills(self, player_id: int) -> dict:
        """Get player's recent kills."""

        return self._get(
            f"{self.base_endpoints['players']}/{player_id}/kills"
        ).json()

    # Seemingly deprecated
    # def get_players_events(self, player_id: int) -> dict:
    #     """Get player's recent events."""

    #     return self._get(
    #         f"{self.base_endpoints['players']}/{player_id}/events"
    #     ).json()

    def get_players_captures(self, player_id: int) -> dict:
        """Get player's flag captures."""

        return self._get(
            f"{self.base_endpoints['players']}/{player_id}/captures"
        ).json()

    def get_players_lookup(self, username: str) -> dict:
        """Find players matching provided name (or part of it)"""

        return self._get(
            f"{self.base_endpoints['players']}/search/{username}"
        ).json()

    def get_players_stats_by_id(self, player_id: int) -> dict:
        """Get player's stats by id."""

        return self._get(
            f"{self.base_endpoints['players']}/{player_id}/basic"
        ).json()

    def get_players_stats_by_username(self, player_name: int) -> dict:
        """Get player's stats by username."""

        return self._get(
            f"{self.base_endpoints['players']}/lookup/{player_name}"
        ).json()

    def get_players_hitters(self, player_id: int) -> dict:
        """Get favorite player's weapons and related stats."""

        return self._get(
            f"{self.base_endpoints['players']}/{player_id}/hitters"
        ).json()

    def get_players_nemesis(self, player_id: int) -> dict:
        """Get whom killed this player the most."""

        return self._get(
            f"{self.base_endpoints['players']}/{player_id}/nemesis"
        ).json()

    def get_players_bullied(self, player_id: int) -> dict:
        """Get whos been killed by this player the most."""

        return self._get(
            f"{self.base_endpoints['players']}/{player_id}/bullied"
        ).json()

    def get_status(self) -> dict:
        """Get overview of this API endpoint."""

        return self._get(f"{self.base_endpoints['root']}/status").json()

    def get_maps(self) -> dict:
        """Get map-related statistics."""

        return self._get(f"{self.base_endpoints['root']}/maps").json()

    def get_servers(self) -> dict:
        """Get active servers."""

        return self._get(self.base_endpoints["servers"]).json()

    def get_servers_info(self, server_id: int) -> dict:
        """Get detailed info of the selected server."""

        return self._get(f"{self.base_endpoints['servers']}/{server_id}").json()

    # Seemingly deprecated
    # def get_servers_events(self, server_id: int) -> dict:
    #     """Get recent server's events."""

    #     return self._get(
    #         f"{self.base_endpoints['servers']}/{server_id}/events"
    #     ).json()

    # Broken atm, see player kills issue above
    # def get_servers_kills(self, server_id: int) -> dict:
    #     """Get recent server's kills."""

    #     return self._get(
    #         f"{self.base_endpoints['servers']}/{server_id}/kills"
    #     ).json()

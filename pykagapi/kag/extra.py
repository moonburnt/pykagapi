from typing import Optional, Tuple, List, Dict, Literal
from .client import KagAPIClient

# Helper methods for api client


def get_alive_servers(
    api_client: KagAPIClient,
    limit: Optional[int] = None,
    start: Optional[int] = None,
) -> dict:
    """Get currently running servers."""

    return api_client.get_servers(
        filters=[{"field": "current", "op": "eq", "value": True}],
        limit=limit,
        start=start,
    )


def get_active_servers(
    api_client: KagAPIClient,
    limit: Optional[int] = None,
    start: Optional[int] = None,
):
    """Get servers with players on them"""

    return api_client.get_servers(
        filters=[
            {"field": "current", "op": "eq", "value": True},
            {"field": "currentPlayers", "op": "ge", "value": 1},
        ],
        limit=limit,
        start=start,
    )

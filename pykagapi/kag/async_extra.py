from typing import Optional, Tuple, List, Dict, Literal
from .async_client import AsyncKagAPIClient

# Helper methods for async api client


async def get_alive_servers(
    api_client: AsyncKagAPIClient,
    # limit: Optional[int] = None,
    # start: Optional[int] = None,
) -> dict:
    """Get currently running servers."""

    return await api_client.get_servers(
        filters=[{"field": "current", "op": "eq", "value": True}],
        # limit=limit,
        # start=start,
    )


async def get_active_servers(
    api_client: AsyncKagAPIClient,
    # limit: Optional[int] = None,
    # start: Optional[int] = None,
):
    """Get servers with players on them"""

    return await api_client.get_servers(
        filters=[
            {"field": "current", "op": "eq", "value": True},
            {"field": "currentPlayers", "op": "ge", "value": 1},
        ],
        # limit=limit,
        # start=start,
    )

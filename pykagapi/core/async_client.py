from aiohttp import ClientSession, ClientTimeout
from typing import Optional, Tuple, List, Dict, Literal


class AsyncAPIClient:
    def __init__(self, api_root: str, timeout: Optional[int] = None):
        self.s = ClientSession(
            timeout=ClientTimeout(total=timeout),
            headers={"user-agent": "pykagapi"},
        )

        self.api_root = api_root
        self.base_endpoints = {
            "root": self.api_root,
        }

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def _get(
        self,
        url,
        auth: Optional[Tuple[str, str]] = None,
        params: Optional[dict] = None,
        validate_status: bool = True,
    ):
        return await self.s.get(
            url,
            auth=auth,
            params=params,
            raise_for_status=validate_status,
        )

    async def close(self):
        await self.s.close()

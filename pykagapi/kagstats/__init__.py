from .client import *
from .async_client import *

# Shared instance for sake of simplicity.
# Feel free to don't use it, if you don't want to
_client = None
_async_client = None


def get_client():
    global _client
    if _client is None:
        _client = KagStatsAPIClient()

    return _client


def get_async_client():
    global _async_client
    if _async_client is None or _async_client.s.closed:
        _async_client = AsyncKagStatsAPIClient()

    return _async_client

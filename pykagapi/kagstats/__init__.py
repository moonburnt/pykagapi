from .client import *


# Shared instance for sake of simplicity.
# Feel free to don't use it, if you don't want to
_client = None


def get_client():
    global _client
    if _client is None:
        _client = KagStatsAPIClient()

    return _client

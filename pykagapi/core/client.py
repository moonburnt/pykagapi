from requests import Session, Response
from typing import Optional, Tuple, List, Dict, Literal
from json import dumps


class SessionWithTimeout(Session):
    def __init__(self, timeout: Optional[int] = None):
        if timeout is None:
            timeout = 30
        self.timeout = timeout

        super().__init__()

    def request(self, method, url: str, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout

        return super().request(method, url, **kwargs)


class APIClient:
    def __init__(self, api_root: str, timeout: Optional[int] = None):
        self.s = SessionWithTimeout(timeout)
        self.s.headers.update({"user-agent": "pykagapi"})

        self.api_root = api_root
        self.base_endpoints = {
            "root": self.api_root,
        }

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def _get(
        self,
        url,
        auth: Optional[Tuple[str, str]] = None,
        params: Optional[dict] = None,
        validate_status: bool = True,
    ) -> Response:
        answer = self.s.get(url, auth=auth, params=params)
        if validate_status:
            answer.raise_for_status()

        return answer

    def close(self):
        self.s.close()

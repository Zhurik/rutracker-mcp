from rutracker_mcp_server.config import config

from .rutracker import Rutrackerer
from .schemas import SearchResult, Torrent

__all__ = [
    "Torrent",
    "SearchResult",
    "Rutrackerer",
]


def get_rutracker_client() -> Rutrackerer:
    return Rutrackerer(
        login=config.rutracker_login,
        password=config.rutracker_password,
    )

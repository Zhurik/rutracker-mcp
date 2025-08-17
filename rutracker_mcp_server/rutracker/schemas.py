import dataclasses
from typing import Any


@dataclasses.dataclass
class SearchResult:
    topic_id: str
    title: str
    size: int
    download_url: str
    seeds: int | None = None
    leeches: int | None = None
    info_hash: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Torrent:
    topic_id: str
    filename: str
    filesize: int
    content_base64: str
    mime_type: str = "application/x-bittorrent"

    def as_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)

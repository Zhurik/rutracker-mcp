import base64
import logging

from py_rutracker import AsyncRuTrackerClient

from . import schemas

logger = logging.getLogger(__name__)


class Rutrackerer:
    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password

    async def search_torrents(self, query: str) -> list[schemas.SearchResult]:
        try:
            async with AsyncRuTrackerClient(self.login, self.password) as client:
                results = await client.search_all_pages(query)
        except Exception as e:
            logger.error(f"Got exception when searching: {e}")
            raise

        try:
            for result in results:
                results.append(schemas.SearchResult(**result))
        except TypeError as e:
            logger.error(f"Error when parsing results: {e}")
            raise

        return results

    async def download_torrent(self, topic_id: str) -> schemas.Torrent:
        try:
            async with AsyncRuTrackerClient(self.login, self.password) as client:
                torrent_data = await client.download(topic_id)
        except Exception as e:
            logger.error(f"Got exception when downloading torrent: {e}")
            raise

        try:
            encoded_torrent_file = base64.b64encode(torrent_data).decode("utf-8")
        except Exception as e:
            logger.error(f"Got exception when encoding torrent: {e}")
            raise

        return schemas.Torrent(
            topic_id=topic_id,
            filename=f"{topic_id}.torrent",
            filesize=len(torrent_data),
            content_base64=encoded_torrent_file,
        )

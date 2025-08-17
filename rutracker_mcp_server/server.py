import logging
from typing import Any

from mcp.server.fastmcp import FastMCP

from .rutracker import get_rutracker_client

logger = logging.getLogger(__name__)

# Create FastMCP server instance
app = FastMCP("rutracker-mcp")


@app.tool()
async def search_torrents(query: str) -> list[dict[str, Any]]:
    """
    Search torrents on RuTracker by query

    Args:
        query: Search query string

    Returns:
        List of found torrents with metadata
    """
    logger.info(f"Searching torrents for query: {query}")

    try:
        client = get_rutracker_client()
        results = await client.search_torrents(query)
        logger.info(f"{len(results)} found")
        return [item.as_dict() for item in results]

    except Exception as e:
        logger.error(f"Error during search: {e}")
        raise RuntimeError(f"Search failed: {str(e)}") from e


@app.tool()
async def download_torrent(topic_id: str) -> dict[str, Any]:
    """
    Download a torrent file from RuTracker by topic ID and return as base64

    Args:
        topic_id: Torrent topic ID

    Returns:
        Dictionary with base64-encoded torrent data and metadata
    """
    logger.info(f"Downloading torrent with ID: {topic_id}")

    try:
        client = get_rutracker_client()
        torrent = await client.download_torrent(topic_id)
        return torrent.as_dict()

    except Exception as e:
        logger.error(f"Error during download: {e}")
        raise RuntimeError(f"Download failed: {str(e)}") from e


if __name__ == "__main__":
    app.run()

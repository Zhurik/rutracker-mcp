import inspect

from rutracker_mcp_server.server import download_torrent, search_torrents


def test_app_has_required_tools():
    """Test that app has the required tools registered"""
    # We can't easily introspect FastMCP tools, so we test the functions directly
    assert callable(search_torrents)
    assert callable(download_torrent)


def test_function_signatures():
    """Test function signatures using introspection"""
    # Test search_torrents signature
    sig = inspect.signature(search_torrents)
    assert "query" in sig.parameters

    # Test download_torrent signature
    sig = inspect.signature(download_torrent)
    assert "topic_id" in sig.parameters

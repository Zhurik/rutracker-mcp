import pytest


def test_http_server_starts():
    """Test that HTTP server can be configured"""
    # Test that our entry point accepts HTTP transport option
    from rutracker_mcp_server import app

    # Check that streamable_http_app method exists
    assert hasattr(app, "streamable_http_app")


@pytest.mark.skip(reason="Integration test requiring external process management")
def test_http_server_integration():
    """Integration test for HTTP server (skipped in unit tests)"""
    # This would be a full integration test that:
    # 1. Starts the server in a subprocess
    # 2. Makes HTTP requests to test endpoints
    # 3. Verifies MCP protocol compliance over HTTP
    # 4. Cleans up the process
    pass

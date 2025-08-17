# RuTracker MCP Server

MCP (Message Control Protocol) server for interacting with RuTracker API.

## Features

- Search torrents on RuTracker
- Download torrents by topic ID (returned as base64)
- Support for both stdio and HTTP transports
- Compatible with Claude and other MCP clients

## Installation

```bash
uv pip install -e .
```

## Configuration

### Required Environment Variables

Set your RuTracker credentials:
```bash
export RUTRACKER_LOGIN="your_username"
export RUTRACKER_PASSWORD="your_password"
```

Or create a `.env` file:
```bash
RUTRACKER_LOGIN=your_username
RUTRACKER_PASSWORD=your_password
```

### Optional Environment Variables

```bash
# Transport mode (can also be set via CLI --transport)
MODE=stdio  # or http

# HTTP server settings (used with --transport http)
HOST=127.0.0.1
PORT=31415

# Debug mode
DEBUG=false
```

## Usage

### Stdio Transport (default)

For use with Claude Desktop or other stdio-based clients:

```bash
# Start with default settings (stdio)
rutracker-mcp

# Or explicitly specify transport
rutracker-mcp --transport stdio
```

### HTTP Transport

For development and testing:

```bash
# Start HTTP server with CLI args
rutracker-mcp --transport http --host 127.0.0.1 --port 31415

# Start HTTP server (using env vars for host/port if set)
rutracker-mcp --transport http
```

### Command Line Options

```
--transport {stdio,http}  Transport protocol (default: stdio or MODE env var)
--host HOST              Host for HTTP server (default: 127.0.0.1 or HOST env var)
--port PORT              Port for HTTP server (default: 31415 or PORT env var)
--debug                  Enable debug logging (default: false or DEBUG env var)
```

## Tools

### search_torrents

Search torrents by query string.

**Arguments:**
- `query` (string): Search query

**Returns:**
Array of torrent objects with metadata.

### download_torrent

Download a torrent file by topic ID and return as base64.

**Arguments:**
- `topic_id` (string): RuTracker topic ID

**Returns:**
Object with base64-encoded torrent data and metadata:
- `topic_id`: Topic ID
- `filename`: Suggested filename
- `filesize`: Size in bytes
- `content_base64`: Base64-encoded torrent file
- `mime_type`: MIME type ("application/x-bittorrent")

## Integration

This server implements the MCP protocol and can be used with any MCP-compatible client,
including Claude Desktop, OpenCode, or custom implementations.

The server supports two transport modes:
1. **stdio** - For direct integration with AI assistants
2. **HTTP** - For development and testing

## Testing

Run tests with pytest:

```bash
# Install test dependencies
uv pip install -e ".[test]"

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src
```

## Development

The server uses the FastMCP framework which provides:
- Automatic JSON Schema generation for tool parameters and return values
- Support for both stdio and HTTP transports
- Built-in tool discovery and calling mechanisms

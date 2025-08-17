# RuTracker MCP Server

MCP (Message Control Protocol) server for interacting with RuTracker API.

## Features

- Search torrents on RuTracker
- Download torrents by topic ID (returned as base64)
- Support for both stdio and HTTP transports
- Compatible with Claude and other MCP clients

## Installation

### Using pip/uv (Recommended)

```bash
# Install with uv
uv pip install rutracker-mcp

# Or with pip
pip install rutracker-mcp
```

### Using Homebrew (macOS)

```bash
# Tap the repository (once)
brew tap YOUR_USERNAME/homebrew-rutracker-mcp

# Install the formula
brew install rutracker-mcp
```

### From source

```bash
git clone https://github.com/YOUR_USERNAME/rutracker-mcp.git
cd rutracker-mcp
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

## Development

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended)

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/rutracker-mcp.git
cd rutracker-mcp

# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Run pre-commit hooks
uv run pre-commit run --all-files
```

### Testing

Run tests with pytest:

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=rutracker_mcp_server
```

### Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality:

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run all hooks on all files
uv run pre-commit run --all-files
```

## CI/CD

The project uses GitHub Actions for continuous integration:
- Pre-commit hooks validation
- Unit tests execution
- Conventional commits enforcement

## Publishing

To publish a new version:
1. Update version in `pyproject.toml`
2. Create a git tag
3. Publish to PyPI
4. Update Homebrew formula

## License

This project is licensed under the MIT License - see the LICENSE file for details.

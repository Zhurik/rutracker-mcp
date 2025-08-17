import logging

import uvicorn
from starlette.applications import Starlette
from starlette.routing import Mount

from .args import get_args
from .config import config
from .server import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Entry point for the rutracker MCP server."""

    args = get_args()

    # Override config with CLI args
    config.mode = args.transport
    config.host = args.host
    config.port = args.port
    config.debug = args.debug

    logger.info(
        f"Using RuTracker credentials from environment: {config.rutracker_login}"
    )

    if config.mode == "stdio":
        logger.info("Starting RuTracker MCP server over stdio")
        app.run(transport="stdio")

    elif config.mode == "http":
        logger.info(
            f"Starting RuTracker MCP server over HTTP at {config.host}:{config.port}"
        )
        # Create Starlette app with our FastMCP app mounted
        starlette_app = Starlette(routes=[Mount("/", app.streamable_http_app())])

        uvicorn.run(
            starlette_app,
            host=config.host,
            port=config.port,
            log_level="debug" if config.debug else "info",
        )


if __name__ == "__main__":
    main()

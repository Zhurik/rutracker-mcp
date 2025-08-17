import argparse
import logging

from .config import config


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RuTracker MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default=config.mode,  # Use config default
        help="Transport protocol (default: stdio)",
    )
    parser.add_argument(
        "--host", default=config.host, help="Host for HTTP server (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=config.port,
        help="Port for HTTP server (default: 31415)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=config.debug,
        help="Enable debug logging",
    )

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    return args

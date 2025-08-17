from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    """Application configuration from environment variables"""

    # RuTracker credentials (required from env)
    rutracker_login: str = Field(
        validation_alias="RUTRACKER_LOGIN", description="RuTracker account username"
    )
    rutracker_password: str = Field(
        validation_alias="RUTRACKER_PASSWORD", description="RuTracker account password"
    )

    # Note: Other settings will come from CLI args, not env vars
    # But we define them here for consistency
    mode: Literal["stdio", "http"] = "stdio"
    host: str = "127.0.0.1"
    port: int = 31415
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )


# Global config instance
config = AppConfig()

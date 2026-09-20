"""Configuration management for PythonAutotest."""

import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass
class BrowserConfig:
    browser_type: str = "chrome"
    headless: bool = True
    timeout: int = 30
    window_width: int = 1920
    window_height: int = 1080
    remote_url: str = ""


@dataclass
class AppConfig:
    base_url: str = field(default_factory=lambda: os.getenv("BASE_URL", "https://example.com"))
    api_url: str = field(default_factory=lambda: os.getenv("API_URL", "https://api.example.com"))
    username: str = field(default_factory=lambda: os.getenv("TEST_USER", "test@example.com"))
    password: str = field(default_factory=lambda: os.getenv("TEST_PASS", "password123"))
    browser: BrowserConfig = field(default_factory=BrowserConfig)
    screenshot_on_failure: bool = True
    video_on_failure: bool = False
    retries: int = 2


config = AppConfig()

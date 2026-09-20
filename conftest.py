"""Pytest configuration and fixtures."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import config


@pytest.fixture(scope="function")
def browser():
    """Create browser instance for each test."""
    if config.browser.browser_type == "firefox":
        options = FirefoxOptions()
        options.headless = config.browser.headless
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        options.headless = config.browser.headless
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={config.browser.window_width},{config.browser.window_height}")
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(config.browser.timeout)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return config.base_url


@pytest.fixture(scope="session")
def api_url():
    return config.api_url

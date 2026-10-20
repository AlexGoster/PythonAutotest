"""Pytest configuration and fixtures."""

import pytest
import os
from threading import Thread
from tests.demo_app import DemoHandler
from http.server import ThreadingHTTPServer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import config


@pytest.fixture(scope="function")
def browser():
    """Create browser instance for each test."""
    if config.browser.browser_type == "firefox":
        options = FirefoxOptions()
        if config.browser.headless:
            options.add_argument("--headless")
    else:
        options = ChromeOptions()
        if config.browser.headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={config.browser.window_width},{config.browser.window_height}")
    if config.browser.remote_url:
        driver = webdriver.Remote(command_executor=config.browser.remote_url, options=options)
    elif config.browser.browser_type == "firefox":
        driver = webdriver.Firefox(options=options)
    else:
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(config.browser.timeout)
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture(scope="session")
def demo_urls():
    if os.getenv("BASE_URL") and os.getenv("API_URL"):
        yield None
        return
    server = ThreadingHTTPServer(("0.0.0.0", 0), DemoHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    old_proxy = os.environ.get("NO_PROXY")
    os.environ["NO_PROXY"] = (old_proxy + "," if old_proxy else "") + "127.0.0.1,localhost"
    port = server.server_port
    try:
        yield (f"http://{os.getenv('DEMO_BROWSER_HOST', '127.0.0.1')}:{port}", f"http://127.0.0.1:{port}")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
        if old_proxy is None:
            os.environ.pop("NO_PROXY", None)
        else:
            os.environ["NO_PROXY"] = old_proxy


@pytest.fixture(scope="session")
def base_url(demo_urls):
    return os.getenv("BASE_URL") or demo_urls[0]


@pytest.fixture(scope="session")
def api_url(demo_urls):
    return os.getenv("API_URL") or demo_urls[1]

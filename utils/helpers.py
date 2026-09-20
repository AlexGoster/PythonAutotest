"""Utility functions for tests."""

import random
import string
import time
from datetime import datetime


def generate_email(domain: str = "test.com") -> str:
    timestamp = int(time.time())
    random_str = "".join(random.choices(string.ascii_lowercase, k=6))
    return f"{random_str}{timestamp}@{domain}"


def generate_string(length: int = 10) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def wait_for_condition(condition, timeout: int = 10, interval: float = 0.5) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if condition():
            return True
        time.sleep(interval)
    return False


def take_screenshot(driver, name: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(path)
    return path

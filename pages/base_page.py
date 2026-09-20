"""Base Page Object with common methods."""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str = ""):
        self.driver = driver
        self.base_url = base_url
        self._wait = WebDriverWait(driver, 15)

    def open(self, path: str = "") -> None:
        self.driver.get(f"{self.base_url}{path}")

    def find(self, locator: tuple) -> object:
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple) -> list:
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple) -> None:
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator: tuple, text: str) -> None:
        element = self._wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self._wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator: tuple, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element(self, locator: tuple, timeout: int = 15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def screenshot(self, name: str) -> str:
        path = f"screenshots/{name}.png"
        self.driver.save_screenshot(path)
        return path

    @property
    def title(self) -> str:
        return self.driver.title

    @property
    def current_url(self) -> str:
        return self.driver.current_url

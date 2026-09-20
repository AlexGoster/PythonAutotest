"""Dashboard page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    URL = "/dashboard"

    USER_AVATAR = (By.CSS_SELECTOR, ".user-avatar")
    NAV_MENU = (By.CSS_SELECTOR, ".nav-menu")
    NOTIFICATIONS_BTN = (By.CSS_SELECTOR, ".notifications")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search']")
    STATS_CARDS = (By.CSS_SELECTOR, ".stat-card")
    LOGOUT_BTN = (By.ID, "logout")

    def open(self) -> None:
        super().open(self.URL)

    def is_loaded(self) -> bool:
        return self.is_visible(self.USER_AVATAR)

    def get_stats_count(self) -> int:
        return len(self.find_all(self.STATS_CARDS))

    def search(self, query: str) -> None:
        self.fill(self.SEARCH_INPUT, query)

    def logout(self) -> None:
        self.click(self.LOGOUT_BTN)

"""Login page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "/login"

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password?")

    def open(self) -> None:
        super().open(self.URL)

    def login(self, email: str, password: str) -> None:
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_visible(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    def click_forgot_password(self) -> None:
        self.click(self.FORGOT_PASSWORD_LINK)

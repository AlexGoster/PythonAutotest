"""Login tests."""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:
    def test_valid_login(self, browser, base_url):
        page = LoginPage(browser, base_url)
        page.open()
        page.login("test@example.com", "password123")
        dashboard = DashboardPage(browser, base_url)
        assert dashboard.is_loaded()

    def test_invalid_email(self, browser, base_url):
        page = LoginPage(browser, base_url)
        page.open()
        page.login("wrong@email.com", "password123")
        assert page.is_error_visible()
        assert "Invalid" in page.get_error_message()

    def test_invalid_password(self, browser, base_url):
        page = LoginPage(browser, base_url)
        page.open()
        page.login("test@example.com", "wrongpass")
        assert page.is_error_visible()

    def test_empty_fields(self, browser, base_url):
        page = LoginPage(browser, base_url)
        page.open()
        page.login("", "")
        assert page.is_error_visible()

    def test_forgot_password_link(self, browser, base_url):
        page = LoginPage(browser, base_url)
        page.open()
        page.click_forgot_password()
        assert "reset" in page.current_url.lower()

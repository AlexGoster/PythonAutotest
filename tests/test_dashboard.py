"""Dashboard tests."""

import pytest
from pages.dashboard_page import DashboardPage


class TestDashboard:
    def test_dashboard_loads(self, browser, base_url):
        page = DashboardPage(browser, base_url)
        page.open()
        assert page.is_loaded()

    def test_stats_visible(self, browser, base_url):
        page = DashboardPage(browser, base_url)
        page.open()
        assert page.get_stats_count() > 0

    def test_search_functionality(self, browser, base_url):
        page = DashboardPage(browser, base_url)
        page.open()
        page.search("test query")
        assert page.current_url

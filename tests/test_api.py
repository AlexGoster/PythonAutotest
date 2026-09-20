"""API integration tests."""

import requests
import pytest


class TestAPI:
    def test_health_endpoint(self, api_url):
        response = requests.get(f"{api_url}/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

    def test_get_users(self, api_url):
        response = requests.get(f"{api_url}/api/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_create_user(self, api_url):
        data = {"email": "new@test.com", "name": "Test User"}
        response = requests.post(f"{api_url}/api/users", json=data)
        assert response.status_code in (200, 201)

    def test_unauthorized_access(self, api_url):
        response = requests.get(f"{api_url}/api/protected")
        assert response.status_code == 401

import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.fetch_weather import fetch_weather_data

# ใช้ monkeypatch เพื่อ mock requests.get
import requests

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

def mock_requests_get(*args, **kwargs):
    return MockResponse({
        "location": {"name": "Bangkok", "country": "Thailand"},
        "current": {"temperature": 30}
    })

def test_fetch_weather_data(monkeypatch):
    # mock requests.get ด้วย mock_requests_get
    monkeypatch.setattr(requests, "get", mock_requests_get)

    result = fetch_weather_data("Bangkok")

    assert isinstance(result, dict)
    assert "location" in result
    assert "current" in result
    assert result["location"]["name"] == "Bangkok"

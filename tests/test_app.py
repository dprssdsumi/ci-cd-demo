import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../app"))

import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "running"

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "healthy"

def test_add(client):
    res = client.get("/add/3/7")
    assert res.status_code == 200
    assert res.get_json()["result"] == 10

def test_subtract(client):
    res = client.get("/subtract/10/4")
    assert res.status_code == 200
    assert res.get_json()["result"] == 6

def test_reverse(client):
    res = client.get("/reverse/hello")
    assert res.get_json()["result"] == "olleh"

def test_reverse_single_char(client):
    res = client.get("/reverse/a")
    assert res.get_json()["result"] == "a"

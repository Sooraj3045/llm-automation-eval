
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "BiteSpeed Support API is running"


def test_late_order():
    response = client.post(
        "/chat",
        json={"message": "My order is late"}
    )

    assert response.status_code == 200
    assert "refund" in response.json()["response"].lower()


def test_delayed_order():
    response = client.post(
        "/chat",
        json={"message": "My delivery is delayed"}
    )

    assert response.status_code == 200
    assert "voucher" in response.json()["response"].lower()


def test_missing_item():
    response = client.post(
        "/chat",
        json={"message": "My item is missing"}
    )

    assert response.status_code == 200
    assert "refund" in response.json()["response"].lower()


def test_unknown_query():
    response = client.post(
        "/chat",
        json={"message": "Tell me about company history"}
    )

    assert response.status_code == 200
    assert "unable to determine" in response.json()["response"].lower()


def test_invalid_request():
    response = client.post(
        "/chat",
        json={}
    )

    assert response.status_code == 422


def test_invalid_endpoint():
    response = client.get("/invalid")

    assert response.status_code == 404

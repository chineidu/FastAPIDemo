from fastapi.testclient import TestClient
from fastapi import status


def test_fetch_one(client: TestClient):
    """This tests that the fetch_one endpoint is working."""
    # Given
    expected_response = {
        "track": "Data Science",
        "mentor": "Chineidu",
        "cost": 350000,
        "company": "Stutern",
    }

    # When
    response = client.get("http://localhost:8000/fetch-one/1/")

    # Then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_add_track(client):
    """This tests that the add_track endpoint is working."""
    # Given
    payload = {
        "track": "Machine Learning Engineering",
        "mentor": "Neidu",
        "cost": 500_000,
        "company": "A big Company",
    }

    # When
    response = client.post(
        "http://localhost:8000/add-track/3",
        json=payload,
    )

    # Then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == payload

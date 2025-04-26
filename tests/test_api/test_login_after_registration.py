import pytest
from urllib.parse import urlencode

@pytest.mark.asyncio
async def test_login_after_registration_unverified_user(async_client, db_session):
    # Register a new user
    response = await async_client.post("/register/", json={
        "email": "newuser@example.com",
        "password": "ValidPass1!",
        "first_name": "New",
        "last_name": "User"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "newuser@example.com"

    # Try to log in before verification
    form_data = {
        "username": "newuser@example.com",
        "password": "ValidPass1!"
    }
    response = await async_client.post(
        "/login/",
        data=urlencode(form_data),
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 403
    assert "email not verified" in response.json().get("detail", "")


from builtins import str
import uuid
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user_base_data["nickname"] = "johnny_d"
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user_create_data["nickname"] = "new_user"
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# ✅ Additional tests for password validation

# Valid passwords
@pytest.mark.parametrize("password", [
    "StrongPass1!",
    "A1b2c3d4$",
    "P@ssword123",
    "Complex*Password9"
])
def test_user_create_valid_passwords(user_base_data, password):
    user_data = {**user_base_data, "password": password, "nickname": "validuser"}
    user = UserCreate(**user_data)
    assert user.password == password

# Invalid passwords
@pytest.mark.parametrize("password", [
    "short1!",          # Too short
    "nouppercase1!",    # Missing uppercase
    "NOLOWERCASE1!",    # Missing lowercase
    "NoNumber!",        # Missing number
    "NoSpecial123",     # Missing special character
])
def test_user_create_invalid_passwords(user_base_data, password):
    user_data = {**user_base_data, "password": password, "nickname": "invaliduser"}
    with pytest.raises(ValidationError):
        UserCreate(**user_data)


# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update_data["first_name"] = "John"
    user_update_data["last_name"] = "Doe"
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# ✅ Additional tests for profile field edge cases

def test_user_update_bio_only(user_update_data):
    user_update_data.clear()
    user_update_data["bio"] = "Updated bio only."
    user = UserUpdate(**user_update_data)
    assert user.bio == "Updated bio only."


def test_user_update_profile_picture_only(user_update_data):
    user_update_data.clear()
    user_update_data["profile_picture_url"] = "https://example.com/pic.jpg"
    user = UserUpdate(**user_update_data)
    assert user.profile_picture_url == "https://example.com/pic.jpg"


def test_user_update_multiple_fields(user_update_data):
    user_update_data.clear()
    user_update_data.update({
        "bio": "Updated bio.",
        "linkedin_profile_url": "https://linkedin.com/in/updateduser"
    })
    user = UserUpdate(**user_update_data)
    assert user.bio == "Updated bio."
    assert user.linkedin_profile_url == "https://linkedin.com/in/updateduser"


def test_user_update_no_fields():
    with pytest.raises(ValidationError):
        UserUpdate()

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user_response_data["id"] = uuid.uuid4()
    user_response = UserResponse(**user_response_data)
    assert user_response.id == user_response_data["id"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login_request_data["email"] = login_request_data.pop("username")
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Tests for UserBase
def test_user_base_invalid_email(user_base_data_invalid):
    with pytest.raises(ValidationError) as exc_info:
        user = UserBase(**user_base_data_invalid)

    assert "value is not a valid email address" in str(exc_info.value)
    assert "john.doe.example.com" in str(exc_info.value)

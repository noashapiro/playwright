import uuid
from dataclasses import dataclass


@dataclass
class FakeUser:
    first_name: str
    last_name: str
    email: str
    password: str


def generate_user():
    uid = uuid.uuid4().hex[:8]
    return FakeUser(
        first_name="Test",
        last_name="User",
        email=f"testuser_{uid}@example.com",
        password="Test@1234",
    )

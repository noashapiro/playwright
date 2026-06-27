from dataclasses import dataclass

from faker import Faker

fake = Faker()


@dataclass
class FakeUser:
    first_name: str
    last_name: str
    email: str
    password: str


def generate_user():
    return FakeUser(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.unique.email(),
        password=fake.password(length=10),
    )

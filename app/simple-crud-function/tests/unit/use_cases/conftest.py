from typing import Optional
from uuid import UUID
import pytest
from use_cases.user_desc import UserDescUseCase
from entities.user import User


class MockUserDescService:
    def describe(self, _id: UUID) -> Optional[User]:
        return None


@pytest.fixture(scope="session")
def user_desc_service() -> MockUserDescService:
    return MockUserDescService()


@pytest.fixture(scope="session")
def user_desc_use_case(user_desc_service: MockUserDescService) -> UserDescUseCase:
    return UserDescUseCase(user_desc_service)

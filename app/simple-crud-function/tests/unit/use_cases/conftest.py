from typing import Optional
from uuid import UUID

import pytest
from entities.user import User
from use_cases.user_desc import UserDescUseCase


class MockUserDescService:
    def describe(self, _id: UUID) -> Optional[User]:
        return None


@pytest.fixture(scope="session")
def user_desc_service() -> MockUserDescService:
    return MockUserDescService()


@pytest.fixture(scope="session")
def user_desc_use_case(user_desc_service: MockUserDescService) -> UserDescUseCase:
    return UserDescUseCase(user_desc_service)

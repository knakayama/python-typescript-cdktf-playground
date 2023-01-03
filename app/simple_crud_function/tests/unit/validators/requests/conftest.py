import pytest

from tests.unit.fixtures import utils


@pytest.fixture(scope="session")
def path_parameters() -> dict[str, str]:
    return {
        (utils.string()): utils.string(),
    }

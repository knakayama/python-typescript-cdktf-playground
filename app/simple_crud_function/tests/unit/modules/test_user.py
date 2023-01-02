from hypothesis import given
from hypothesis.strategies import text
from modules import user


class TestUserModule:
    @given(text())
    def test_given_middle_name(self, s: str) -> None:
        assert user.to_name(s, s, s) == f"{s}, {s}, {s}"

    @given(text())
    def test_given_no_middle_name(self, s: str) -> None:
        assert user.to_name(s, None, s) == f"{s} {s}"

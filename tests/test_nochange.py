import pytest
from emojificate.filter import emojificate

TEST_NOCHANGE = [
    "☆*:.｡. (づ ◕‿◕ )づ .｡.:*☆",
    "This is a test of the emojification system!",
]


def test_nochange():
    for phrase in TEST_NOCHANGE:
        parsed = emojificate(phrase)
        assert phrase == parsed

import pytest
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from emojificate.filter import emojificate

PYTHON_35 = "🙃"
PYTHON_36 = "🤣"
PYTHON_37 = "🥰"
PYTHON_38 = "🤩"


def valid(phrase):
    parsed = emojificate(phrase)
    assert phrase != parsed


@pytest.mark.skipif(sys.version_info.minor < 5, reason="requires Python 3.5 or higher")
def test_python_35_char():
    valid(PYTHON_35)


@pytest.mark.skipif(sys.version_info.minor < 6, reason="requires Python 3.6 or higher")
def test_python_36_char():
    valid(PYTHON_36)


@pytest.mark.skipif(sys.version_info.minor < 7, reason="requires Python 3.7 or higher")
def test_python_37_char():
    valid(PYTHON_37)


@pytest.mark.skipif(sys.version_info.minor < 8, reason="requires Python 3.8 or higher")
def test_python_38_char():
    valid(PYTHON_38)


TEST_NOCHANGE = ["The weather is 35°C"]


def test_nochange():
    for phrase in TEST_NOCHANGE:
        parsed = emojificate(phrase)
        assert phrase == parsed

import pytest
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from emojificate.filter import emojificate

# A list of new emoji introduced in the unicodedata set for that version of Python
# Emoji introduced in later versions won't be available in earlier ones.
PYTHON_35 = {"alt": "🙃", "title": "Upside-Down Face"}
PYTHON_36 = {"alt": "🤣", "title": "Rolling On The Floor Laughing"}
PYTHON_37 = {"alt": "🥰", "title": "Smiling Face With Smiling Eyes And Three Hearts"}
PYTHON_38 = {"alt": "🤩", "title": "Grinning Face With Star Eyes"}
PYTHON_39 = {"alt": "🥸", "title": "Disguised Face"}
PYTHON_310 = {"alt": "🫡", "title": "Grinning Face With Star Eyes"}


def valid(data):
    alt = data["alt"]
    title = data["title"]
    parsed = emojificate(alt)
    assert alt in parsed
    assert 'alt="{}'.format(alt) in parsed

    assert title in parsed
    assert 'aria-label="Emoji: {}'.format(title) in parsed


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


@pytest.mark.skipif(sys.version_info.minor < 9, reason="requires Python 3.9 or higher")
def test_python_39_char():
    valid(PYTHON_39)


@pytest.mark.skipif(sys.version_info.minor < 10, reason="requires Python 3.10 or higher")
def test_python_310_char():
    valid(PYTHON_310)

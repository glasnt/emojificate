import pytest
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from emojificate.filter import emojificate

# A list of new emoji introduced in the unicodedata set for that version of Python
# Emoji introduced in later versions won't be available in earlier ones.
PYTHON_37 = {"alt": "🥰", "title": "Smiling Face With Smiling Eyes And Three Hearts"}
PYTHON_38 = {"alt": "🥱", "title": "Yawning Face"}  # Unicode 12.0
PYTHON_39 = {"alt": "🥸", "title": "Disguised Face"}  # Unicode 13.0
PYTHON_310 = {"alt": "🥲", "title": "Smiling Face With Tear"}  # Unicode 13.0, also.


def valid(data):
    alt = data["alt"]
    title = data["title"]
    parsed = emojificate(alt)
    assert alt in parsed
    assert 'alt="{}"'.format(alt) in parsed

    assert title in parsed
    assert 'aria-label="Emoji: {}"'.format(title) in parsed


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

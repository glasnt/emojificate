import pytest
from emojificate.filter import emojificate


def valid(emoji, title, fuzzy=False):
    parsed = emojificate(emoji)

    assert emoji in parsed
    assert 'alt="{}'.format(emoji) in parsed

    assert title in parsed
    if not fuzzy:
        assert 'aria-label="Emoji: {}'.format(title) in parsed


def test_flag():
    valid("🇦🇺", "Australia", fuzzy=True)


def test_pride():
    valid("🏳️‍🌈", "Rainbow Flag")


def test_farmer():
    valid("👩🏼‍🌾", "Woman Farmer Medium-Light Skin Tone")

import pytest
from emojificate.filter import emojificate


def valid(emoji, title):
    parsed = emojificate(emoji)

    assert emoji in parsed
    assert 'alt="{}'.format(emoji) in parsed

    assert title in parsed
    assert 'aria-label="Emoji: {}'.format(title) in parsed


def test_flag():
    valid("🇦🇺", "Flag For Australia")


def test_pride():
    valid("🏳️‍🌈", "Rainbow Flag")


def test_farmer():
    valid("👩🏼‍🌾", "Woman Farmer Medium-Light skin tone")

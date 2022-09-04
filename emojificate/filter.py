import unicodedata
from grapheme import graphemes
import emoji
import requests


__all__ = ["emojificate"]

cdn_fmt = "https://twemoji.maxcdn.com/v/latest/72x72/{codepoint}.png"


def valid_src(src):
    req = requests.head(src)
    return req.status_code == 200


def valid_category(char):
    try:
        return unicodedata.category(char) == "So"
    except TypeError:
        return False


def get_best_name(char):
    """
    unicode data does not recognise the grapheme, 
    so try and parse something from emoji instead.
    """
    shortcode = emoji.demojize(char, language='alias')

    # Roughly convert shortcode to screenreader-friendly sentence.
    return shortcode.replace(":", "").replace("_", " ").replace("selector", "").title()


def convert(char):
    def tag(a, b):
        return '%s="%s"' % (a, b)

    def codepoint(codes):
        # See https://github.com/twitter/twemoji/issues/419#issuecomment-637360325
        if "200d" not in codes:
            return "-".join([c for c in codes if c != "fe0f"])
        return "-".join(codes)

    if valid_category(char):
        # Is a Char, and a Symbol
        name = unicodedata.name(char).title()
    else:
        if len(char) == 1:
            # Is a Char, not a Symbol, we don't care.
            return char
        else:
            # Is probably a grapheme
            name = get_best_name(char)

    src = cdn_fmt.format(codepoint=codepoint(["{cp:x}".format(cp=ord(c)) for c in char]))

    # If twitter doesn't have an image for it, pretend it's not an emoji.
    if valid_src(src):
        return "".join(
            [
                "<img",
                tag(" src", src),
                tag(" alt", char),
                tag(" title", name),
                tag(" aria-label", "Emoji: %s" % name),
                ">",
            ]
        )
    else:
        return char


def emojificate(string):
    return "".join(convert(ch) for ch in graphemes(string))

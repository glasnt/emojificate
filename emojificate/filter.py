import unicodedata


__all__ = ['emojificate']


cdn = "https://twemoji.maxcdn.com/36x36/"
cdn_ft = ".png"


def tag(a, b):
    return "%s=\"%s\"" % (a, b)


def convert(char):
    if unicodedata.category(char) == "So":
        name = unicodedata.name(char).title()
        code = char.encode("unicode_escape").decode("utf-8")[2:].strip("0")
        return "".join([
            "<img",
            tag(" src", cdn + code + cdn_ft),
            tag(" alt", char),
            tag(" title", name),
            tag(" aria-label", "Emoji: %s" % name),
            ">"
        ])
    else:
        return char


def emojificate(line):
    return ''.join(convert(ch) for ch in line)

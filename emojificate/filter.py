import unicodedata


__all__ = ['emojificate']


cdn_fmt = "https://twemoji.maxcdn.com/36x36/{codepoint:x}.png"  # {:x} gives hex


def tag(a, b):
    return "%s=\"%s\"" % (a, b)


def convert(char):
    if unicodedata.category(char) == "So":
        name = unicodedata.name(char).title()
        return "".join([
            "<img",
            tag(" src", cdn_fmt.format(codepoint=ord(char))),
            tag(" alt", char),
            tag(" title", name),
            tag(" aria-label", "Emoji: %s" % name),
            ">"
        ])
    else:
        return char


def emojificate(line):
    return ''.join(convert(ch) for ch in line)

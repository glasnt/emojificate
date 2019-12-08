import unicodedata
import requests


__all__ = ['emojificate']

cdn_fmt = "https://twemoji.maxcdn.com/v/12.1.4/72x72/{codepoint:x}.png"  # {:x} gives hex

def valid_src(src):
    req = requests.head(src)
    print(src)
    print(req.status_code)
    return req.status_code == 200

def valid_category(char):
    if unicodedata.category(char) == "So":
        return True
    else:
        return False

def tag(a, b):
    return "%s=\"%s\"" % (a, b)


def convert(char):
    if valid_category(char):
        name = unicodedata.name(char).title()

        src = cdn_fmt.format(codepoint=ord(char))

        if valid_src(src):
            return "".join([
                "<img",
                tag(" src", src),
                tag(" alt", char),
                tag(" title", name),
                tag(" aria-label", "Emoji: %s" % name),
                ">"
            ])
        else:
            return char
    else:
        return char


def emojificate(line):
    return ''.join(convert(ch) for ch in line)

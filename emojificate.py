import unicodedata
import sys

def display_help():
    print("emojificate.py -- turns text with emoji into text with accessible emoji")

cdn = "https://twemoji.maxcdn.com/36x36/"
cdn_ft = ".png"

def tag(a,b):
    return "%s=\"%s\"" % (a,b)

def emojificate(line):
    result = ""

    for char in line:
        append = char
        if unicodedata.category(char) == "So":
             name = unicodedata.name(char).title()
             code = char.encode("unicode_escape").decode("utf-8")[2:].strip("0") 
             append = "".join(["<img", 
                                tag(" src", cdn+code+cdn_ft), 
                                tag(" alt", char), 
                                tag(" title", name), 
                                tag(" aria-label", "Emoji: %s" % name),
                                ">"])
                
        result += append
    return result

if __name__ == "__main__": 
    line = " ".join(sys.argv[1:])
    if line:
        print(emojificate(line))
    else: 
        display_help()
        sys.exit(1)

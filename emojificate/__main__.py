import sys

from .filter import emojificate


def display_help():
    print("emojificate.py -- turns text with emoji into text with accessible emoji")


if __name__ == "__main__":
    line = " ".join(sys.argv[1:])
    if line:
        print(emojificate(line))
    else:
        display_help()
        sys.exit(1)

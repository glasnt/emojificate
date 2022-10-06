import sys
import click

from .filter import emojificate
from .defaults import DEFAULT_CSS_CLASS, DEFAULT_FILETYPE


@click.command()
@click.argument("input_string")
@click.option(
    "--filetype", help="File type for image (PNG, SVG)", default=DEFAULT_FILETYPE
)
@click.option(
    "--css-class", help="CSS class to use for images", default=DEFAULT_CSS_CLASS
)
def cli(input_string, filetype, css_class):
    """emojificate.py -- turns text with emoji into text with accessible emoji"""
    print(emojificate(input_string, filetype=filetype.lower(), css_class=css_class))


if __name__ == "__main__":
    cli()

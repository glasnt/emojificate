from django.template import Library, Node
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.conf import settings

from ..filter import emojificate
from ..defaults import DEFAULT_CSS_CLASS, DEFAULT_FILETYPE

register = Library()

filetype = DEFAULT_FILETYPE
if hasattr(settings, "EMOJIFICATE_FILETYPE"):
    filetype = settings.EMOJIFICATE_FILETYPE.lower()

css_class = DEFAULT_CSS_CLASS
if hasattr(settings, "EMOJIFICATE_CSS_CLASS"):
    css_class = settings.EMOJIFICATE_CSS_CLASS


@register.filter("emojificate", needs_autoescape=True)
def emojificate_filter(content, autoescape=True):
    """Convert any emoji in a string into accessible content."""
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(emojificate(esc(content), filetype=filetype, css_class=css_class))


@register.tag("emojified")
def do_emojified(parser, token):
    nodelist = parser.parse(("endemojified",))
    parser.delete_first_token()
    return EmojifiedNode(nodelist)


class EmojifiedNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return emojificate(output, filetype=filetype, css_class=css_class)

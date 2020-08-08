from django.template import Library, Node
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from ..filter import emojificate


register = Library()


@register.filter("emojificate", needs_autoescape=True)
def emojificate_filter(content, autoescape=True):
    "Convert any emoji in a string into accessible content."
    # return mark_safe(emojificate(content))
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(emojificate(esc(content)))


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
        return emojificate(output)

import django
import os

from django.template import Context, Template
from django.conf import settings

settings.configure(
    INSTALLED_APPS=["emojificate"],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(os.path.dirname(__file__), "templates")],
        }
    ],
)
django.setup()


TEST_FILTER = """
{% load emojificate %}
This is some {{ user_content|emojificate }} that has emoji in it.
"""

TEST_TAG = """
{% load emojificate %}
{% emojified %}
This is some template content that 💜 emoji as well.
{% endemojified %}
"""


def valid(data):
    assert "emoji" in data
    assert "alt" in data


def test_filter():
    context = Context({"user_content": "✨"})

    parsed = Template(TEST_FILTER).render(context)
    valid(parsed)


def test_tag():
    parsed = Template(TEST_TAG).render(Context())
    valid(parsed)

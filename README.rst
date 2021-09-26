emojificate
===========

|status| |release| |date|
 
.. |status| image:: https://img.shields.io/github/workflow/status/glasnt/emojificate/pytest?label=pytest&style=flat-square   :alt: GitHub Workflow Status

.. |release| image:: https://img.shields.io/github/v/release/glasnt/emojificate?sort=semver&style=flat-square   :alt: GitHub release (latest SemVer)

.. |date| image:: https://img.shields.io/github/release-date/glasnt/emojificate?style=flat-square   :alt: GitHub Release Date

Emojificate is a Python implementation of a concept of using fallback images, alt text, title text and aria labels to represent emoji in HTML, a more accessible method than browser defaults. 

Installation
------------

emojificate is available on pypi::

    pip install emojificate

Usage
-----

To convert a string from the command line::

    $ python3 -m emojificate "I 💜 emoji 😊"
    I <img src="https://twemoji.maxcdn.com/v/12.1.4/72x72/1f49c.png" alt="💜"
    title="Purple Heart" aria-label="Emoji: Purple Heart"> emoji <img
    src="https://twemoji.maxcdn.com/v/12.1.4/72x72/1f60a.png" alt="😊"
    title="Smiling Face With Smiling Eyes" aria-label="Emoji: Smiling Face With
    Smiling Eyes">

Or, if you've got a Django project, put ``emojificate`` into your ``INSTALLED_APPS``, and then use the following in a template::

    {% load emojificate %}
    This is some {{ user_content|emojificate }} that has emoji in it.

    {% emojified %}
    This is some template content that 💜 emoji as well.
    {% endemojified %}

Implementation
--------------

TL;DR: Take a string, split it into tokens, and if a token is emoji, process it into a nice format.

As of 0.4.0, string-splitting is now handled by `grapheme <https://github.com/alvinlindstam/grapheme>`__.

Given a list of tokens, we can leverage the native `unicodedata <https://docs.python.org/3/library/unicodedata.html>`__ to:

* see if a token is a unicode Symbol (an emoji)
* get the codepoint for the emoji, and
* get the name of the emoji.

If a token is a grapheme and not a character, there won't be a record of what it is in unicodedata. In that case emojificate defaults to a human-readable version of the shortcode provided by `emoji <https://github.com/carpedm20/emoji>`__. 

From there, we construct an ``<img>`` replacement for the emoji:

* Use images from `twemoji <https://github.com/twitter/twemoji>`__, Twitter's emoji set (if the URL exists)
* Have an ``alt`` parameter containing the original emoji. This allows for copying-pasting.
* Use the name of the emoji in the ``title`` parameter. This allows for hover-tooltips.
* Add an ``aria-label`` for screen-reader accessibility.

For more information, see `Solve For Emoji <https://glasnt.com/blog/solve-for-emoji/>`__.

Implementation in other languages
---------------------------------

Ruby
~~~~~

.. code-block:: ruby

    require 'gemoji'

    def cdn
        "https://twemoji.maxcdn.com/v/latest/72x72/"
    end

    def emojificate(string)
      string.split("").each do |s|
          e = Emoji.find_by_unicode(s)
          if e then
               u = s.ord.to_s(16) # e.g. 1f431
               d = e.description  # e.g. "cat face"
               img = "<img src=\"#{cdn}/#{u}.png\" alt=\"#{s}\" title=\"#{d}\" aria-label=\"Emoji: #{d}\">"
               print img
           else
               print s
           end
       end
     end

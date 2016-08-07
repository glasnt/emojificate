# emojificate

Emojificate is a Python implementation of a concept of using fallback images, alt text, title text and aria labels to represent emoji in HTML code in a more accessible method.

## Usage

```shell
$ python3 emojificate.py I 💜 emoji 😊
```
Result:
> I <img src="https://twemoji.maxcdn.com/36x36/1f49c.png" alt="💜" title="Purple Heart" height="16px" aria-label="Emoji: Purple Heart"> emoji <img src="https://twemoji.maxcdn.com/36x36/1f60a.png" alt="😊" title="Smiling Face With Smiling Eyes" height="16px" aria-label="Emoji: Smiling Face With Smiling Eyes">

## Implementation

TL;DR: Take a string, split it into token, and if a token is emoji, process it into a nice format. 

Splitting the string is a problem, because at the moment it **does not handle Zero Width Joining sequences**. However, native Python string tokenization does work for the most part. 

Given a list of tokens, we can leverage the native [unicodedata](https://docs.python.org/3/library/unicodedata.html) to: 

 * see if a token is a unicode Symbol (an emoji)
 * get the codepoint for the emoji, and
 * get the name of the emoji

From there, we construct an `<img>` replacement for the emoji: 

 * Use images from [twemoji](https://github.com/twitter/twemoji), Twitter's emoji set
 * Have an `alt` parameter containing the original emoji. This allows for copying-pasting. 
 * Use the name of the emoji in the `title` parameter. This allows for hover-tooltips.
 * Add an `aria-label` for screen-reader accessibility. 

For more information, see [Solve For Emoji](http://glasnt.com/blog/2016/08/06/solve-for-emoji.html)

## Limitations

 * Does not handle Zero Width Join Sequences; for example: 🖐🏽, 👩‍👩‍👧

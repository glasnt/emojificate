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

Using [uniseq's](http://uniseg-python.readthedocs.io/en/latest/graphemecluster.html#uniseg.graphemecluster.grapheme_clusters) implementation of the [Unicode Text Segmentation](http://www.unicode.org/reports/tr29/tr29-21.html) standard, we can split a string into separate tokens.

Leveraging the native [unicodedata](https://docs.python.org/3/library/unicodedata.html) we can: 

 * see if a token is a unicode Symbol (an emoji)
 * get the codepoint for the emoji, and
 * get the name of the emoji

From there, we construct an `<img>` replacement for the emoji: 

 * Use images from [twemoji](https://github.com/twitter/twemoji), Twitter's emoji set
 * Have an `alt` parameter containing the original emoji. This allows for copying-pasting. 
 * Use the name of the emoji in the `title` parameter. This allows for hover-tooltips.
 * Add an `aria-label` for screen-reader accessibility. 

For more information, see [Solve For Emoji](glasnt.com/blog/2016/08/06/solve-for-emoji.html)


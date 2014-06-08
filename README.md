[SoPins](http://sopins.heroku.com/)
=================

Social badges on the fly. A fork of [pypins](https://github.com/badges/pypipins) by [karan](http://github.com/karan) ([@karangoel](http://twitter.com/karangoel)).

| Tweet | Like | Share |
| ----- | ---- | ----- | 
| ![](http://sopins.herokuapp.com/twitter/http://www.goel.im/pin.png) | ![](http://sopins.herokuapp.com/facebook/like/http://www.goel.im/pin.png) | ![](http://sopins.herokuapp.com/facebook/share/http://www.goel.im/pin.png) |

Example badges for `http://www.goel.im/`.

## Usage

### Tweet

    http://sopins.herokuapp.com/twitter/<url>/pin.<format>

  Example:

    http://sopins.herokuapp.com/twitter/https://www.google.com/pin.png

  Example that open Tweet popup:

    [![](http://sopins.herokuapp.com/twitter/https://www.google.com/pin.png)](https://twitter.com/intent/tweet?text=This+is+Amazing.&amp;url=http://www.goel.im&amp;via=KaranGoel)

  This renders to: [![](http://sopins.herokuapp.com/twitter/https://www.google.com/pin.png)](https://twitter.com/intent/tweet?text=This+is+Amazing.&amp;url=http://www.goel.im&amp;via=KaranGoel)

### Facebook

  **1. Share**

    http://sopins.herokuapp.com/facebook/like/<url>/pin.<format>

  Example:

    http://sopins.herokuapp.com/facebook/share/https://www.google.com/pin.png

  Example that open Share popup:

    [![](http://sopins.herokuapp.com/facebook/share/https://www.google.com/pin.png)](https://www.facebook.com/sharer/sharer.php?u=http://www.goel.im)

  This renders to: [![](http://sopins.herokuapp.com/facebook/share/https://www.google.com/pin.png)](https://www.facebook.com/sharer/sharer.php?u=http://www.goel.im)

  **2. Like**

    http://sopins.herokuapp.com/facebook/share/<url>/pin.<format>

  Example:

    http://sopins.herokuapp.com/facebook/like/https://www.google.com/pin.png

## Formats

SoPins are available in variety of formats:

- PNG
- SVG
- JPEG
- GIF
- TIFF

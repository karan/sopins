[SoPins](http://sopins.heroku.com/)
=================

Social badges on the fly. A fork of [pypins](https://github.com/badges/pypipins) by [karan](http://github.com/karan) ([@karangoel](http://twitter.com/karangoel)).

| Tweet | Like | Share |
| ----- | ---- | ----- | 
| ![](http://sopins.herokuapp.com/twitter/http://www.goel.io/pin.png) | ![](http://sopins.herokuapp.com/facebook/like/http://www.goel.io/pin.png) | ![](http://sopins.herokuapp.com/facebook/share/http://www.goel.io/pin.png) |

Example badges for `http://www.goel.im/`.

## Usage

### Tweet

    http://sopins.herokuapp.com/twitter/<url>/pin.<format>

  Example:

    http://sopins.herokuapp.com/twitter/https://www.google.com/pin.png

  Example that open Tweet popup:

    [![](http://sopins.herokuapp.com/twitter/https://www.google.com/pin.png)](https://twitter.com/intent/tweet?text=This+is+Amazing.&amp;url=http://www.goel.im&amp;via=KaranGoel)

  This renders to: [![](http://sopins.herokuapp.com/twitter/https://www.google.com/pin.png)](https://twitter.com/intent/tweet?text=This+is+Amazing.&amp;url=http://www.goel.im&amp;via=KaranGoel)

###LinkedIn

  ```
  http://sopins.herokuapp.com/linkedin/<url>/pin.<format>
  ```

  Example:
  ```
  http://sopins.herokuapp.com/linkedin/http://arstechnica.com/pin.png
  ```
  

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

##Styles 

SoPins has support for different styles for the pins, you can use either `flat` (default) , `plastic` and `flat-square` styles for your pins.

Using different styles is very easy, you just need to enter a style parameter in your URL. 

For example:

```
http://sopins.herokuapp.com/facebook/like/https://www.google.com/pin.png?style=flat-square
```

```
http://sopins.herokuapp.com/linkedin/http://arstechnica.com/pin.png?style=plastic
```

```
http://sopins.herokuapp.com/linkedin/https://github.com/pin.png?style=flat
```
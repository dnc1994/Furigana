# Furigana

Help you add [furigana](https://en.wikipedia.org/wiki/Ruby_character) to your Japanese notes.

## Usage

Write your notes like this:

```
[今度]{こんど}こそ[君]{きみ}だけは[幸]{しあわ}せにしてみせる
```

Run the script:

```
python furigana.py [note1.md note2.md ...]
```

You get:

```
<ruby>今度<rp>（</rp><rt>こんど</rt><rp>）</rp></ruby>こそ<ruby>君<rp>（</rp><rt>きみ</rt><rp>）</rp></ruby>だけは<ruby>幸<rp>（</rp><rt>しあわ</rt><rp>）</rp></ruby>せにしてみせる
```

Which renders to:

<ruby>今度<rp>（</rp><rt>こんど</rt><rp>）</rp></ruby>こそ<ruby>君<rp>（</rp><rt>きみ</rt><rp>）</rp></ruby>だけは<ruby>幸<rp>（</rp><rt>しあわ</rt><rp>）</rp></ruby>せにしてみせる

The original file would be saved in a `.bak` before the conversion.

## Note

1. For the the `<ruby>` tag to render properly, the browser must support it. See [HTML <ruby> Tag](http://www.w3schools.com/tags/tag_ruby.asp).
2. Currently, in order to **precisely** map furigana to kanji, you'll have to split kanji into individual ones manually. I'm trying to develop some matching algorithms here but the subtlety of kanji makes it terribly complicated to do so. Help me if you think you know how to do it smartly.

## Author
[Linghao Zhang](https://github.com/dnc1994)

## License
[MIT license](https://github.com/dnc1994/SSCIP/blob/master/LICENSE)

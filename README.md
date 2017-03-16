# sha1-collision
Googleが発表したSHA-1衝突の原理で衝突PDFを生成するスクリプト

## About

## Files
* collision.py -> 衝突PDF生成スクリプト．二つの画像を入力とする．
* collision-1.pdf, collision-2.pdf -> 衝突させたPDF．
* sample1.jpg, sample2.jpg -> PDFに埋め込むJPG．何でも良い．
* materials -> 必要なバイナリデータを入れてるディレクトリ．
* example_figs -> 成功例画像

## Usage
```
$ python collision.py sample1.jpg sample2.jpg
```

## Mechanism
* 以下のスライドがとても参考になります．
* https://www.slideshare.net/herumi/googlesha1

## Limitation
* Adobeのリーダだと見れないことがあるのでブラウザで見るのが良い．pdfの方のフォーマットの関係と思われます．そこについては未実装．
* サイズによっては横に伸びたり縦に伸びたりしそう．そこは衝突とはあまり関係ないため実装するかは迷いどころです．

## Example
* 1つ目の画像のPDFのハッシュ値が2つ目の画像．別々のPDFにも関わらず衝突していることが分かる．
* 3つ目はバイナリエディタで手動で書き換えたやつ．こちらは参考にした既存の衝突PDFと同じ大きさの画像を使っているためAdobeで開ける．

![example1](https://github.com/73spica/sha1-collision/blob/master/example_figs/sha1-collision-neta.PNG)


![example2](https://github.com/73spica/sha1-collision/blob/master/example_figs/sha1.PNG)


![example3](https://github.com/73spica/sha1-collision/blob/master/example_figs/sha1-collision.PNG)

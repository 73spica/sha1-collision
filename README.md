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

## Example

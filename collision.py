#! coding:utf-8
# SHA-1衝突PDFを自動生成するスクリプト

import sys
from Crypto.Util.number import bytes_to_long as b2l
from Crypto.Util.number import long_to_bytes as l2b


def main():
    # コマンドライン引数でファイル名とか受け取る
    if len(sys.argv) != 3:
        print "Usage : python collision.py <衝突PDF1に使うJPG画像> <衝突pdf2に使うJPG画像>"
        sys.exit(1)

    # 引数のファイルがJPGかどうか確認
    jpg1 = open(sys.argv[1],"r").read()
    jpg2 = open(sys.argv[2],"r").read()
    format_error = False

    print b2l(jpg1[:2])
    if b2l(jpg1[:2])!=0xffd8:
        print sys.argv[1],"is not JPG format."
        format_error = True
    if b2l(jpg2[:2])!=0xffd8:
        print sys.argv[2],"is not JPG format."
        format_error = True
    if format_error:
        sys.exit(1)

    print "correct"

    # JPGだということがわかったらもう FF D8 はいらないので捨てる
    jpg1 = jpg1[2:]
    jpg2 = jpg2[2:]

    # 初期宣言
    # 各マーカー値とかくっつけるバイナリを保存してるファイル名とか

    # マーカー値
    # ffは全部に共通してるのでifのところで個別に見ればいいかな
    SOI = 0xd8      # JPEG開始
    EOI = 0xd9      # JPEG終了
    APP0 = 0xe0     # JFIF
    COM = 0xfe      # コメント
    SOS = 0xda      # スキャン開始
    FC = 0x00fc     # 分かりやすくするため00付けてる

    HEADER1_FILE = "./materials/header1.bin" # 一つ目のpdfの先頭部分
    HEADER2_FILE = "./materials/header2.bin" # 二つ目のpdfの先頭部分
    FOOTER_FILE = "./materials/footer.bin"   # 二つの画像データの後に来る末尾の部分

    header1 = open(HEADER1_FILE,"r").read()
    header2 = open(HEADER2_FILE,"r").read()
    footer  = open(FOOTER_FILE,"r").read()


    # ===== 細工部分 =====
    # まず，画像1の細工からやる．
    size = len(jpg1)
    pos = 0
    pre_pos = pos
    result = ""
    first_f = True
    while pos < size:
        c0 = ord(jpg1[pos])
        if c0 == 0xff:
            c1 = ord(jpg1[pos+1])
            if c1 == SOS:
                if first_f:
                    print "Find,It's first:",pos
                    result += jpg1[:pos].encode("hex") # とりあえず ffe0 ~ ffda直前までを入れる
                    pre_pos = pos
                    first_skip = pos
                    pos += 2
                    first_f = False
                    continue
                comment_area = pos - pre_pos + 4 + 2 # fffe0006の後までにしたいので4足す．fe後の2バイト-2がコメントになるので2足す．
                insert = 0xfffe0006fffe0000 + comment_area
                result += hex(insert)[2:-1] + jpg1[pre_pos:pos].encode("hex")
                print "Find:",pos
                pre_pos = pos
                pos += 2
            else:
                pos += 1
        else:
            pos += 1
    #print result
    comment_area = pos - pre_pos + 2 # fffe0006の後までにしたいので4足す．fe後の2バイト-2がコメントになるので2足す．
    insert = 0xfffe0006fffe0000 + comment_area
    result += hex(insert)[2:-1] + jpg1[pre_pos:pos].encode("hex")
    result = result.decode("hex")

    # 次に，先頭部分のFF FE 00 FCの部分の00FCを書き換えて，うまく次のFF FE 00 06のところまで行くようにバイト数を計算して埋め込む
    comment_area = 8 + first_skip + 4 + 2
    insert = ("fffe"+format(comment_area,"04x")+"00"*8).decode("hex")
    print insert.encode("hex")

    # 細工した値と必要な値をがっちゃんこして.pdfで保存して完成
    open("collision-1.pdf","w").write(header1+insert+result+jpg2+footer)
    open("collision-2.pdf","w").write(header2+insert+result+jpg2+footer)


if __name__ == "__main__":
    main()

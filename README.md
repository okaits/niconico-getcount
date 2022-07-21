# niconico-getcount
## 概要
ニコニコ動画の特定の動画の視聴回数と、視聴回数が伸びるスピードを取得できます。

## 使い方
視聴回数を取得する:
```bash
$ python3 getniconicocount.py sm...
```
スピード, スピード平均(プログラム開始から計測開始)を取得する
```bash
$ python3 getniconicocountspeed.py sm...
```

### 出力の意味
getniconicocount.pyの出力
Equal: aaaaa   取得した情報が前回取得したものと同じことを表します。
UP-aa: bbbbb   aaは前回取得した値との差、bbbbbは現在の視聴回数を表します。

getniconicocountspeed.pyの出力
INIT aaaaa, 0c/m プログラムの実行直後に表示されます。
SPEED aaac/m     スピードがaaa回/分であることを表します。
AVG aa.aaaac/m   スピード平均がaaa.aaaa回/分であることを表します。

## 注意事項
* このプログラムはニコニコ動画の`getthumbinfo`というAPIを使用しています。並列に動かすとニコニコ動画のサーバーに負荷がかかってしまうので、控えたほうが良いと思います。
* 素人が作ったプログラムなので、動作が不安定な可能性があります。
* 出力結果が不正確な可能性があります。

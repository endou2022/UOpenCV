# -*- coding:utf-8 -*-

# sample program for UOpenCV

import cv2
from UOpenCV import UOpenCV  # UOpenCV.pyからクラスを読み込む

fname = '球状黒鉛鋳鉄.jpg'
img1 = UOpenCV(fname).imshow().grayscale().medianBlur(ksize=5).threshold().bitwise_not().labeling_paint(minsize=100).imshow()
'''
UOpenCV(fname)               ファイルを読み込んでオブジェクトを作る
imshow()                     画像を表示（タイトルの日本語は文字化けする）
grayscale()                  グレースケール変換
medianBlur(ksize=5)          メディアンフィルタでノイズ除去
threshold()                  単純2値化　閾値=128
bitwise_not()                白黒反転　OPenCVは「白」を処理する
labeling_paint(minsize=100)  面積100以上をラベリングして色を塗る
imshow()                     ラベリング結果の表示
'''
print(img1.num)              # 面積>=100 の物体の総数
print('No  x  y  w  h  size')
print(img1.selected_stats)   #「物体」の諸元出力
img1.waitKey()

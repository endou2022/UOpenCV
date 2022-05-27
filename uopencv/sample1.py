# -*- coding:utf-8 -*-

# sample program for UOpenCV

import sys

from UOpenCV import UOpenCV  # UOpenCV.pyからクラスを読み込む
import UOpenCVUtil

if len(sys.argv) == 2:       # コマンドライン、プログラムファイルへのドラッグ＆ドロップ対応
    fname = sys.argv[1]
else:
    fname = 'lena.png'

img1 = UOpenCV(fname).imshow().calcHist()
UOpenCVUtil.showHist(img1, title='BGR輝度ヒストグラム', block=True)  # block=Trueでないとうまく表示できない
img1.grayscale().imshow().threshold().imshow()
'''
UOpenCV(fname)           画像読み込み
imshow()                 画像表示
calcHist()               ヒストグラム集計
UOpenCVUtil.showHist()   ヒストグラム表示  block=True なので、グラフを消すまで待機
grayscale()              グレースケール変換
imshow()                 画像表示
threshold()              単純2値化
imshow()                 画像表示
'''
img1.waitKey()  # キー入力があるまで待つ

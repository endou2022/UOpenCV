# -*- coding:utf-8 -*-

# sample program for UOpenCV
import statistics

import cv2
from UOpenCV import UOpenCV  # UOpenCV.pyからクラスを読み込む

img1 = UOpenCV('colony_count.jpg').imshow().grayscale().threshold().labeling_paint(minsize=20).imshow()

'''
UOpenCV('colony_count.jpg')  ファイルを読み込んでオブジェクトを作る
imshow()                     画像を表示（タイトルの日本語は文字化けする）
grayscale()                  グレースケール変換
threshold()                  単純2値化　閾値=128
labeling_paint(minsize=20)   面積20以上をラベリングして色を塗る
imshow()                     ラベリング結果の表示
'''
colony = [x for x in img1.selected_stats[:, 5] if x < 100]  # 大きすぎるものを除く
print('個々の面積')
print(colony)
print('個数 = {} 平均 = {} 中央値 = {} 標準偏差={:5.1f}'.format(len(colony), statistics.mean(colony), statistics.median(colony), statistics.pstdev(colony)))
img1.waitKey()

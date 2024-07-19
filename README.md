# UOpenCV -- opencv-pythonのラッパークラス

## UOpenCVについて
| 項目 | 内容 |
|:---|:---|
|ソフト名|UOpenCV<br>opencv-pythonのラッパークラス|
|著作権・作者 |FINAL mail address|
|対応ＯＳ|たぶんOS非依存|
|動作確認|Windows10|
|作成日|2022/10/01|
|必要な物|Python<br>opencv-python<br>opencv-contrib-python  (opencv-python と opencv-contrib-pythonは同時に入れる必要がある)|
|種別|フリーソフトウェア|
|ライセンス|BSDライセンス (2021/09/30確認)|
|インストール|「pip install UOpenCV」でインストールするか、[UOpenCV.py](https://pypi.org/project/UOpenCV/) をダウンロードする。|

## 特徴
- UOpenCV とは、OpenCV のラッパークラスです。opencv-python の関数の一部(＋本やホームページにあった画像処理)をクラス化して(作者にとって)使いやすくしました。
- 画像処理ソフトを作るために作ったクラスです。画像処理ソフトとは独立していますので、クラスを利用して色々なソフトを作ることができます。
- ほとんどの関数が画像オブジェクト(UOpenCV)を返しますので、メソッドチェーンを作ることができます。
- 原則として、メソッドは名前引数で呼び出します。
- ほとんどの関数のパラメータが調整してあり、デフォルトのままで使うことができます。

## 詳細な説明
[詳細な説明](uopencv/readme/index.html)です。<br>
HTML形式ですので、全体をダウンロードして読んでください。<br>
[AT-Image](https://www.vector.co.jp/soft/winnt/art/se336426.html) UOpenCVを利用して作ったソフトです。<br>
画像処理の勉強に利用できます。

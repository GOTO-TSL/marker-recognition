# 色検出で軌道をプロット
## 概要
特定の色の物体を検出し，その物体の描く軌道をプロットするスクリプトです．
![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/84612341/132169089-053ee6dd-4948-4e1a-b012-87065dd4514b.gif)
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/84612341/132169166-25f91546-b01a-49dd-99a9-b4b1931a8b97.gif)

## 使用ライブラリ
* OpenCV
* Numpy

## 使い方
### 1. リポジトリをクローンする
```
git clone https://github.com/GOTO-TSL/marker-recognition.git
```
### 2. ライブラリのインストール
お手持ちのpython3環境にopenCVとnumpyをインストールしてください

### 3. 動画ファイルを準備
使用したい動画ファイルをcolor_recognition.pyと同じディレクトリ内に入れてください．
<p>サンプル動画ファイルがリポジトリ内に入っているのでそれを使っても大丈夫です．　</p>

```python:color_recognition.py
def main():
    #動画の読み込み
    mov_file = "動画ファイル名"
    ...
```
mov_file変数に動画ファイル名を入力してください　　

### 4. 検出したい物体の色をHSVで指定

```python:color_recognition.py
def red_detect(img):
    #HSVでの色抽出
    RED_MIN = np.array([150, 150, 20])
    RED_MAX = np.array([180, 255, 255])
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, RED_MIN, RED_MAX)
    return mask
```
red_detect関数内にあるHSV空間のしきい値設定のパラメータをお好みの色に調節してください　　

### 5. 実行
実行するとウィンドウが立ち上がって軌道がプロットされる動画が確認できます．　　color_recognition.pyの２２行目　　

```python:color_recognition.py
 max_index = np.argmax(stats[:,4])
```
でエラーが出る場合は，動画内に指定された色が検出されていない可能性があるので4に戻って調整するとうまくいくと思います．　　

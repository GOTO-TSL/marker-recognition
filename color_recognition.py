import cv2
import numpy as np

def red_detect(img):
    #HSVでの色抽出
    RED_MIN = np.array([150, 150, 20])
    RED_MAX = np.array([180, 255, 255])
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, RED_MIN, RED_MAX)
    return mask

def get_center(binary_img):
    #ラベリング処理
    nlabels, labels, stats, center = cv2.connectedComponentsWithStats(binary_img)

    #背景のオブジェクト情報の削除
    nlabels = nlabels - 1
    stats = np.delete(stats, 0, 0)
    center = np.delete(center, 0, 0)

    #面積が最大のオブジェクトのラベル番号を取得
    max_index = np.argmax(stats[:,4])

    center_x = int(center[max_index][0])
    center_y = int(center[max_index][1])

    return (center_x, center_y)

def drawObit(tracks, new_point, frame):
    tracks.append(new_point)
    for track in tracks:
        cv2.circle(frame, track, 5, (0, 255, 0), thickness=-1)


def main():
    #動画の読み込み
    mov_file = "triangle.MOV"
    cap = cv2.VideoCapture(mov_file)

    #中心座標を格納するリスト
    center_tracks = []

    #保存する動画の設定
    frame_rate = 30
    size = (int(cap.get(3)), int(cap.get(4)))
    fmt = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    writer_video = cv2.VideoWriter("result_triangle_draw.mp4", fmt, frame_rate, size)

    while cap.isOpened():
        #フレームを取得
        ret, frame = cap.read()

        if ret:
            #色抽出用のマスク画像生成
            mask = red_detect(frame)

            #ラベリング処理を行い中心座標を取得
            center = get_center(mask)

            #軌道をプロット
            drawObit(center_tracks, center, frame)

            #動画ファイルに書き込み
            writer_video.write(frame)

            #ウィンドウに表示
            cv2.imshow("draw", frame)
            cv2.imshow("mask", mask)

            #Qキーを押すと止まる
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            break   
    #いろいろ閉じる
    writer_video.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
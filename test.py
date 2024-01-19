import cv2
cv2.nameWindow("frame")

def main():
    # USBカメラにアクセスするためのキャプチャオブジェクトを作成
    cap = cv2.VideoCapture(0)  # 0はカメラのデバイス番号で、通常はUSBカメラが0となります

    # カメラが正常にオープンされたかを確認
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            # カメラからフレームを取得
            ret, frame = cap.read()

            # フレームの取得が失敗した場合、ループを終了
            if not ret:
                print("Error: Failed to capture frame.")
                break

            # 取得したフレームを表示
            cv2.imshow('frame', frame)

            # 'q'キーが押されたらループを終了
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # プログラム終了時にはカメラを解放
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

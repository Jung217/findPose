import cv2
import mediapipe as mp
import math
import numpy as np
import csv

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# 計算兩點之間的角度
def calculate_angle(a, b, c):
    a = np.array(a)  # 第一點
    b = np.array(b)  # 第二點（關節）
    c = np.array(c)  # 第三點

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

# 讀取影片
cap = cv2.VideoCapture("D:/Downloda/t1.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# CSV 檔案設定
csv_file = open('joint_data.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Frame', 'Left Knee Angle', 'Right Knee Angle', 'Waist X', 'Waist Y', 'Waist Z'])  # 寫入 CSV 標題

# Mediapipe Pose 設定
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            # 取得關節角度
            left_knee_angle = calculate_angle(
                [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y],
                [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y],
                [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            )
            right_knee_angle = calculate_angle(
                [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y],
                [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y],
                [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            )

            # 取得腰部（髖關節）的 XYZ 座標
            waist_x = (landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x + landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x) / 2
            waist_y = (landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y + landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y) / 2
            waist_z = (landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z + landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z) / 2

            # 記錄到 CSV 檔案
            csv_writer.writerow([frame_count, left_knee_angle, right_knee_angle, waist_x, waist_y, waist_z])

            # 畫出骨架
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
            )

        # 寫入影片
        out.write(frame)

        # 顯示結果影像
        cv2.imshow('Pose Detection', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

        frame_count += 1

cap.release()
out.release()
csv_file.close()
cv2.destroyAllWindows()
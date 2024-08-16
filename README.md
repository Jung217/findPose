# findPose
My way to try poses

## Intro
> 如果你也覺得 OpenPose 很難搞，正在尋找替代方案，以下一些可供參考：

1. **[MediaPipe](https://github.com/google/mediapipe)**
   - **描述**：由 Google 提供的跨平台框架，支持人體姿勢、手部和面部追蹤等功能。
   - **優點**：高效、準確，支持多平台（包括 Android、iOS 和 Web）。
   - **e.g.**：[DEMO](https://mediapipe-studio.webapps.google.com/home)
2. **[PoseNet](https://github.com/tensorflow/tfjs-models/tree/master/posenet)**
   - **描述**：由 Google 提供的深度學習模型，用於實時人體姿勢估計。
   - **優點**：輕量級，適用於移動設備，提供多種預訓練模型。
3. **[HRNet (High-Resolution Network)](https://github.com/HRNet)**
   - **描述**：一個專注於高分辨率特徵學習的姿勢估計模型，能夠提供精確的姿勢估計。
   - **優點**：能夠在高分辨率圖像上進行準確的姿勢估計。
4. **[AlphaPose](https://github.com/MVIG-SJTU/AlphaPose)**
   - **描述**：一個高效的多人姿勢估計工具，支持高精度的姿勢檢測。
   - **優點**：提供多種模型和高效的檢測能力。
5. **[DeepCut / DeepLabCut](https://github.com/DeepLabCut/DeepLabCut)**
   - **描述**：專注於動物姿勢估計，適合於動物行為分析。
   - **優點**：針對動物姿勢進行高度專業化的研究和應用。
6. **[OpenPifPaf](https://github.com/vita-epfl/openpifpaf)**
   - **描述**：用於實時人體姿勢估計的開源工具，基於 PIFu 和 PIFPaf 模型。
   - **優點**：提供高精度和實時的姿勢估計。

## Try
0. OpenPose : failed (on colab)
1. MediaPipe : 手掌、手勢、全身辯識
   * `pip install tensorflow==2.17.0 mediapipe==0.10.14`

## Research
* [countAngle.py](research/countAngle.py)
1. **新增腰部 (髖關節) 的 XYZ 座標記錄**：計算並記錄腰部位置，包含 X、Y、Z 三個座標。
2. **骨架繪製**：使用 mp_drawing 將骨架畫在影像上。
3. **CSV 檔案**：將每一幀的膝蓋角度和腰部座標記錄到 CSV 檔案中。
4. **確認骨架完整性**：檢查所有的骨架點是否可見，只有當所有點的可見度大於0.5時才進行記錄和計算。
5. **計算人體面積並切割**：計算出人體的邊界框，將人體從影像中切割出來並保存為 PNG 圖像。
6. **保留骨架繪製功能**：在確認骨架完整後，仍然會在影像中繪製骨架。

這樣的邏輯確保只有在骨架完整時，才會進行記錄和切割操作，以提高結果的準確性和資料的完整性。

## Reference
* STEAM 教育學習網
   * [Mediapipe 手掌特徵點偵測](https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe-2023-hand.html)
   * [Mediapipe 辨識比中指，自動馬賽克](https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe-finger-mosaic.html)
   * [Mediapipe 姿勢偵測](https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe-pose.html)

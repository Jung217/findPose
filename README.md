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
00. OpenPose : failed (on colab)
01. MediaPipe : 手掌、手勢、全身辯識

## Reference
* STEAM 教育學習網
   * [Mediapipe 手掌特徵點偵測](https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe-2023-hand.html)
   * [Mediapipe 辨識比中指，自動馬賽克](https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe-finger-mosaic.html)
   * [Mediapipe 姿勢偵測](https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe-pose.html)

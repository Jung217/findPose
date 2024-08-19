## Installation
1. `git clone https://github.com/leoxiaobin/deep-high-resolution-net.pytorch.git`
2. `cd deep-high-resolution-net.pytorch && pip install -r requirement.txt`
3.  `mkdir \models\pytorch\pose_coco`, then download `pose_hrnet_w32_384x288.pth` from [here](https://drive.google.com/drive/folders/1nzM_OBV9LbAEA7HClC0chEyf_7ECDXYA) and put into the folder
4. `python demo/demo.py --video Myvideo.mp4 --showFps --write`

For more detail, check [here](https://github.com/leoxiaobin/deep-high-resolution-net.pytorch/tree/master/demo)
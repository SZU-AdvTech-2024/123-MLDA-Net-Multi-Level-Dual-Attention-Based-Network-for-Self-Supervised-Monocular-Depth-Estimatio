# MLDA-Net
## Installation
Step 1: Install MLDA-Net
```shell
git clone https://github.com/bitcjm/MLDA-Net-repo.git
cd MLDA-Net
conda create -name mldanet python=3.8
conda activate mldanet
```
Step 2: Install necessary packages
```shell
pip install munch
pip install scikit-image
pip install natsort
```
Step 3: Install Paddle(2.5.0rc1.post118)
download from the [link](https://paddle-wheel.bj.bcebos.com/2.5.0-rc1/linux/linux-gpu-cuda11.8-cudnn8.6-mkl-gcc8.2-avx/paddlepaddle_gpu-2.5.0rc1.post118-cp38-cp38-linux_x86_64.whl).
```shell
pip install paddlepaddle_gpu-2.5.0rc1.post118-cp38-cp38-linux_x86_64.whl
```
## Data preparation

### 1. Download Kitti dataset
You can download the full dataset of depth from /splits/kitti_archives_to_download.txt and put them under /data in the following structure.
```
|-- data
  |-- 2011_09_26
  		|-- 2011_09_26_drive_0001_sync
			|-- image_00
        |--data
        |--timestamps.txt
			|-- image_01
			|-- image_02
			|-- image_03
      |-- oxts
      |-- velodyne_points
		|-- 2011_09_26_drive_0002_sync
			|-- ...
		|-- 2011_09_26_drive_0005_sync
			|-- ...
		|-- 2011_09_26_drive_0009_sync
		    |-- ...
    |-- ...
		|-- calib_cam_to_cam.txt
		|-- calib_imu_to_velo.txt
		|-- calib_velo_to_cam.txt
  |-- 2011_09_28
    ...
  |-- 2011_09_29
    ...
  |-- 2011_09_30
    ...
  |-- 2011_10_03
    ...
```

If you only want to download the some dataset, you can download from /splits/kitti_archives_to_download_lite.txt.

### 2. Generate depth_hint
You should generate [depth_hint](https://github.com/nianticlabs/depth-hints) and put them under /data.

## Training
To train model, you can use follow command:
```shell
python train.py --data_path MLDA-Net-repo/data --depth_hint_path MLDA-Net-repo/data/depth_hints --split eigen_full
```
The train.log folder is generated in the MLDA-Net-repo/log_train/ folder(you can change it using --log_dir **) during training and is used to keep training logs.
The trained model parameters are stored in the MLDA-Net-repo/log_train/models.

Training is performed by default with an image size of 640×192 and a network of Resnet18.

## Testing
 ```shell
 python test.py --data_path MLDA-Net-repo/data --depth_hint_path MLDA-Net-repo/data/depth_hints --split eigen_full --load_weights_floder MLDA-Net-repo/log_train/models/best_weights
 ```
If you want to test on your own supplied model, modify the parameter --load_weights_folder your_weight_folder

* Single Image Testing
 ```shell
python predict.py --load_weights_folder MLDA-Net-repo/log_train/models/best_weights
 ```

## Code Structure Description
```
MLDA-Net-repo/ 
    |-- data/               # data
    |-- dataset/            # data preprocessing
    |-- networks/           # model-related code
    |-- losses/             # loss function
    |-- utils/              # tools
    |-- test_tipc/          # tipc related files
    |-- splits/             # the splits of train and test
    |-- log_train/          # the log of train 
      |-- trainer.py/       # the class of train and test
      |-- train.py/         # train model
      |-- test.py           # test model
      |-- predict.py        # signal image test
      |-- export.py         # generate model
      |-- inference.py      # tipc inference
      |-- readme.md         # Description Documentation
```

## Citation
```
@ARTICLE{9416235,
  author={Song, Xibin and Li, Wei and Zhou, Dingfu and Dai, Yuchao and Fang, Jin and Li, Hongdong and Zhang, Liangjun},
  journal={IEEE Transactions on Image Processing}, 
  title={MLDA-Net: Multi-Level Dual Attention-Based Network for Self-Supervised Monocular Depth Estimation}, 
  year={2021},
  volume={30},
  pages={4691-4705},
  keywords={Estimation;Training data;Feature extraction;Cameras;Benchmark testing;Sensors;Image sensors;Depth estimation;self-supervised;dual-attention;feature fusion},
  doi={10.1109/TIP.2021.3074306}}
  ```
  
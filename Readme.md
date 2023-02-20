# 基于MMDetection3D的单目3D目标检测的最小实现版本

## 0. 介绍
本项目是基于mmdetection3d-v1.0.0rc5版本实现的用于单目3D目标检测的最小版本，命名为:
[mono-mmdet3d-mini](https://github.com/Xiaolong-RRL/mono-mmdet3d-mini)
- 从头开始进行系统构建
- 仅保留了单目3D算法相关的代码
- 其余结构和官方完全一致

## 1. 使用
使用方式与官方[MMDetection3D-v1.0.0rc5](https://github.com/open-mmlab/mmdetection3d/tree/v1.0.0rc5)
完全一致

### 安装
参考官方文档：[getting_started](docs/getting_started.md)
```shell script
# 在Anaconda中新建虚拟环境
conda create -n mmdet3d python=3.7 -y
conda activate mmdet3d

# 安装最新的PyTorch版本
conda install -c pytorch pytorch torchvision -y

# install mmcv
pip install mmcv-full

# install mmdetection
pip install git+https://github.com/open-mmlab/mmdetection.git

# install mmsegmentation
pip install git+https://github.com/open-mmlab/mmsegmentation.git

# install mono-mmdet3d-mini
git clone https://github.com/Xiaolong-RRL/mono-mmdet3d-mini.git
cd mmdetection3d
pip install -v -e . # or "python setup.py develop"
# -v：verbose, or more output
# -e：editable，修改本地文件，调用的模块以最新文件为准
```

### 数据准备
参考官方文档：[data_preparation](docs/data_preparation.md)
```
mono-mmdet3d-mini
├── mmdet3d
├── tools
├── configs
├── data
│   ├── kitti
│   │   ├── ImageSets
│   │   ├── testing
│   │   │   ├── calib
│   │   │   ├── image_2
│   │   │   ├── velodyne
│   │   ├── training
│   │   │   ├── calib
│   │   │   ├── image_2
│   │   │   ├── label_2
│   │   │   ├── velodyne
```
推荐使用软连接将KITTI数据集连接到data文件夹下：
```shell script
ln -s [源文件] [本目录文件]
```

### 训练(仅支持单卡)
```shell
python tools/train.py ${CONFIG_FILE} [optional arguments]
# 例如训练SMOKE：python tools/train.py configs/smoke/smoke_dla34_pytorch_dlaneck_gn-all_8x4_6x_kitti-mono3d.py
```

### 测试
```shell
python tools/test.py ${CONFIG_FILE} ${CHECKPOINT_FILE} [--out ${RESULT_FILE}] [--eval ${EVAL_METRICS}] [--show] [--show-dir ${SHOW_DIR}]
# 例如测试SMOKE：python tools/test.py configs/smoke/smoke_dla34_pytorch_dlaneck_gn-all_8x4_6x_kitti-mono3d.py work_dirs/smoke_dla34_pytorch_dlaneck_gn-all_8x4_6x_kitti-mono3d/latest.pth --show --show-dir ./outputs/smoke/smoke_kitti
```


## 2. 模型

| Model   | Supported          |
| :-----: | :----------------: |
| [SMOKE](https://arxiv.org/pdf/2002.10111.pdf)   | :white_check_mark: |
| [MonoCon](https://arxiv.org/pdf/2112.04628.pdf) | :x:                |
| [MonoDLE](https://arxiv.org/pdf/2103.16237.pdf) | :white_check_mark: |
| [GUPNet](https://arxiv.org/pdf/2107.13931.pdf)  | :x:                |
| [DID-M3D](https://arxiv.org/pdf/2207.08531.pdf) | :x:                |


## 3. 规划
### Done
- kitti数据转换
- 搭建起基于SMOKE和KITTI的单目3D目标检测训练流程
- 搭建起基于MonoCon和KITTI的单目3D目标检测训练流程

### Doing
- 优化代码，去除无关和冗余代码，并在通用代码处添加详细注释和解析文档

### To-list
- 支持PGD的完整训练、测试和可视化流程
- 支持MonoDLE、GUPNet、DID-M3D的完整训练、测试和可视化流程

## 4. 更新日志
- 2023.2.10: 发布初版
- 2023.2.13: 支持SMOKE训练
- 2023.2.19: 支持MonoCon训练

## 5. 致谢
- [MMDetection3D官方文档](https://mmdetection3d.readthedocs.io/zh_CN/latest/)

- [MMDetection3D-v1.0.0rc5](https://github.com/open-mmlab/mmdetection3d/tree/v1.0.0rc5)

- [MonoCon](https://github.com/Xianpeng919/MonoCon)

- [mmdetection-mini](https://github.com/hhaAndroid/mmdetection-mini)


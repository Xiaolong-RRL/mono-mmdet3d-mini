# 基于MMDetection3D的单目3D目标检测的最小实现版本

## 0.介绍
本项目是基于mmdetection3d-v1.0.0rc5版本实现的用于单目3D目标检测的最小版本，命名为:
[Mono-MMDet3d-Mini](https://github.com/Xiaolong-RRL/Mono-MMDet3d-Mini)
- 从头开始进行系统构建
- 仅保留了单目3D算法相关的代码
- 其余结构和官方完全一致

## 1.规划
1. 首先搭建起基于SMOKE和KITTI的单目3D目标检测完整流程
2. 优化代码，去除无关和冗余代码，并在通用代码处添加详细注释和解析文档
3. 支持MonoCon的完整训练、测试和可视化流程
4. 支持PGD的完整训练、测试和可视化流程
5. 支持MonoDLE、GUPNet、DID-M3D的完整训练、测试和可视化流程

## 2.模型
- [x] SMOKE
- [x] MonoCon
- [ ] MonoDLE
- [ ] GUPNet
- [ ] DID-M3D

## 3.进度
### 3.1 Done
- kitti数据转换
- 搭建起基于SMOKE和KITTI的单目3D目标检测训练流程
- 搭建起基于MonoCon和KITTI的单目3D目标检测训练流程

### 3.2 Doing
- 优化代码，去除无关和冗余代码，并在通用代码处添加详细注释和解析文档

### 3.3 To-list
- 支持PGD的完整训练、测试和可视化流程
- 支持MonoDLE、GUPNet、DID-M3D的完整训练、测试和可视化流程

## 4.更新日志
- 2023.2.10: 发布初版
- 2023.2.13: 支持SMOKE训练
- 2023.2.19: 支持MonoCon训练

## 5.致谢
- [MMDetection3D官方文档](https://mmdetection3d.readthedocs.io/zh_CN/latest/)

- [MMDetection3D-v1.0.0rc5](https://github.com/open-mmlab/mmdetection3d/tree/v1.0.0rc5)

- [MonoCon](https://github.com/Xianpeng919/MonoCon)

- [mmdetection-mini](https://github.com/hhaAndroid/mmdetection-mini)


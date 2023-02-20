# Copyright (c) OpenMMLab. All rights reserved.
from mmdet.core.bbox import build_bbox_coder
from .smoke_bbox_coder import SMOKECoder

__all__ = [
    'build_bbox_coder', 'SMOKECoder'
]

_base_ = [
    './monocon_dla34_200e_kitti_train.py'
]

model = dict(
    bbox_head=dict(
        type='MonoConHeadInference',
    )
)

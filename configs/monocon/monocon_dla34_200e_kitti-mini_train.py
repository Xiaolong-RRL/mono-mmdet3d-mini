_base_ = [
    '../_base_/models/monocon.py',
    '../_base_/datasets/kitti-mini-monocon.py',
    '../_base_/schedules/cyclic_200e_monocon.py',
    '../_base_/default_runtime.py'
]

checkpoint_config = dict(interval=20)
evaluation = dict(interval=10)
workflow = [('train', 1)]

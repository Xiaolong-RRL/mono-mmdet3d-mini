_base_ = [
    '../_base_/datasets/kitti-smoke.py', '../_base_/models/smoke.py',
    '../_base_/default_runtime.py'
]

# 每隔10轮训练保存一次权重
checkpoint_config = dict(interval=12)
# 每隔两轮训练验证一下指标
evaluation = dict(interval=10)

# optimizer
optimizer = dict(type='Adam', lr=2.5e-4)
optimizer_config = dict(grad_clip=None)
lr_config = dict(policy='step', warmup=None, step=[50])

# runtime settings
runner = dict(type='EpochBasedRunner', max_epochs=72)
log_config = dict(interval=50)

find_unused_parameters = True

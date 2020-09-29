_base_ = [
    '../_base_/models/deeplabv3_r50-d8-std-supervised_imagenet100_e2000_pyres.py', '../_base_/datasets/cityscapes.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]

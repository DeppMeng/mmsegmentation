_base_ = [
    '../_base_/models/deeplabv3_r50-d8-std-train_epoch_1_pyres.py', '../_base_/datasets/cityscapes.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
_base_ = [
    '../_base_/models/deeplabv3_r50-d8-std-supervised_v2_f_e200_pyres.py', '../_base_/datasets/cityscapes.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
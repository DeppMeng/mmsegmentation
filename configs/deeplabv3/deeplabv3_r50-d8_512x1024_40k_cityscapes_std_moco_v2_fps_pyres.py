_base_ = [
    '../_base_/models/deeplabv3_r50-d8-std-moco_v2_fps_pyres.py', '../_base_/datasets/cityscapes.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
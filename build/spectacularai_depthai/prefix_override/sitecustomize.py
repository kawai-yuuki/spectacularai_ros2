import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yuukikawai-kamlab/spectacularai_ros2/install/spectacularai_depthai'

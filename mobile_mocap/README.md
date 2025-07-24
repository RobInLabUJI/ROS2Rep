# Mobile Motion Capture

## Original code repository
[https://github.com/RIVeR-Lab/mobile_mocap](https://github.com/RIVeR-Lab/mobile_mocap)

## Citation
```
@INPROCEEDINGS{10260562,
  author={Lvov, Gary and Zolotas, Mark and Hanson, Nathaniel and Allison, Austin
          and Hubbard, Xavier and Carvajal, Michael and Padir, Taşkin},
  booktitle={2023 IEEE 19th International Conference on Automation Science and Engineering (CASE)}, 
  title={Mobile MoCap: Retroreflector Localization On-The-Go}, 
  year={2023},
  volume={},
  number={},
  pages={1-7},
  keywords={Location awareness;Tracking;Robot vision systems;Pose estimation;
            Systems architecture;Cameras;Motion capture},
  doi={10.1109/CASE56687.2023.10260562}}
```

## Status
2025/07/24: Compilation errors.
```
Starting >>> mobile_mocap
--- stderr: mobile_mocap                         
CMake Error at /opt/ros/humble/share/rosidl_cmake/cmake/rosidl_generate_interfaces.cmake:93 (message):
  rosidl_generate_interfaces() the passed file 'msg/Benchmark.msg' doesn't
  exist relative to the CMAKE_CURRENT_SOURCE_DIR
  '/colcon_ws/src/mobile_mocap'
Call Stack (most recent call first):
  CMakeLists.txt:27 (rosidl_generate_interfaces)
---
Failed   <<< mobile_mocap [1.72s, exited with code 1]
```

# ROS2Rep
ROS2 Reproducible Research Repositories

Reproducible [Docker](https://www.docker.com/) images of [ROS 2](https://www.ros.org/) code repositories from [major RAS conferences](https://www.ieee-ras.org/conferences-workshops) between 2019 and 2024.

## Prerequisites
* [Docker](https://docs.docker.com/engine/install/ubuntu/)
* [OSRF/Rocker](https://github.com/osrf/rocker)
* For GPU Docker images: [NVIDIA Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

Tested on Ubuntu 24.04.2 LTS with Docker version 28.3.2, build 578ccf6 and OSRF/Rocker 0.2.19.

## Instructions

Clone this repository:
```
git clone https://github.com/RobInLabUJI/ROS2Rep.git
```
In a terminal:
1. Change to one of the directories
```
cd <folder>
```
2. Build or pull the Docker image
```
./build.sh
```
```
./pull.sh 
```
3. Run a container
```
./run.sh
```

## Status of the repositories

| Repository              | Compilation | Execution |
|------------------------:|:-----------:|:---------:|
| [co-lrio](https://github.com/RobInLabUJI/ROS2Rep/tree/main/co-lrio)                                 | &#x2705;    | &#x2705;  |
| [drive](https://github.com/RobInLabUJI/ROS2Rep/tree/main/drive)                                     | &#x2705;    | &#x274C;  |
| [drl_grasping](https://github.com/RobInLabUJI/ROS2Rep/tree/main/drl_grasping)                       | &#x274C;    | &#x2705;  |
| [fogros2](https://github.com/RobInLabUJI/ROS2Rep/tree/main/fogros2)                                 | &#x2705;    | &#x274C;  |
| [l3gs](https://github.com/RobInLabUJI/ROS2Rep/tree/main/l3gs)                                       | &#x274C;    | &#x274C;  |
| [mobile_mocap](https://github.com/RobInLabUJI/ROS2Rep/tree/main/mobile_mocap)                       | &#x274C;    | &#x274C;  |
| [moveit_task_constructor](https://github.com/RobInLabUJI/ROS2Rep/tree/main/moveit_task_constructor) | &#x2705;    | &#x2705;  |
| [navigation2](https://github.com/RobInLabUJI/ROS2Rep/tree/main/navigation2)                         | &#x2705;    | &#x2705;  |
| [patchwork-plusplus](https://github.com/RobInLabUJI/ROS2Rep/tree/main/patchwork-plusplus)           | &#x2705;    | &#x2705;  |
| [racecar_data](https://github.com/RobInLabUJI/ROS2Rep/tree/main/racecar_data)                       | &#x2705;    | &#x2705;  |

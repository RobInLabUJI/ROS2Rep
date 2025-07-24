# ROS2Rep
ROS2 Reproducible Research Repositories

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

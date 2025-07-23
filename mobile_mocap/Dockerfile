FROM osrf/ros:humble-desktop-full

RUN apt-get update && apt-get install -y \
      v4l-utils python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install opencv-python

RUN pip install scikit-spatial

RUN apt-get update && apt-get install -y \
      ros-humble-image-common && \
    rm -rf /var/lib/apt/lists/*

RUN pip install PySimpleGui

RUN mkdir -p /colcon_ws/src

RUN cd /colcon_ws/src \
 && git clone --branch main https://github.com/RIVeR-Lab/mobile_mocap

RUN cd /colcon_ws/src \
 && apt update \
 && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y \
 && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"] 

RUN cd /colcon_ws \
 && source /opt/ros/humble/setup.bash \
 && colcon build


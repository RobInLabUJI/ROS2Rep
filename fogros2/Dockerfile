FROM osrf/ros:humble-desktop-full

RUN apt-get update && apt-get install -y \
      awscli && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /colcon_ws/src

RUN cd /colcon_ws/src \
 && git clone --branch humble https://github.com/BerkeleyAutomation/FogROS2

RUN cd /colcon_ws/src \
 && apt update \
 && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y \
 && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"] 

RUN cd /colcon_ws \
 && source /opt/ros/humble/setup.bash \
 && colcon build


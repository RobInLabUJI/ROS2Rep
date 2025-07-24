FROM osrf/ros:humble-desktop-full

RUN mkdir -p /colcon_ws/src

RUN cd /colcon_ws/src \
 && git clone https://github.com/norlab-ulaval/DRIVE.git \
 && git clone https://github.com/norlab-ulaval/norlab_controllers_ros.git

RUN cd /colcon_ws/src \
 && apt update \
 && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y \
 && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"] 

RUN cd /colcon_ws \
 && source /opt/ros/humble/setup.bash \
 && colcon build



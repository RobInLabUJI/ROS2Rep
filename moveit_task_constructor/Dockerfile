FROM osrf/ros:jazzy-desktop-full

RUN apt-get update && apt-get install -y \
      python3-vcstool && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /ws_moveit2/src

RUN cd /ws_moveit2/src \
 && git clone --branch main https://github.com/ros-planning/moveit2_tutorials \
 && vcs import < moveit2_tutorials/moveit2_tutorials.repos

RUN cd /ws_moveit2/src \
 && apt update \
 && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y \
 && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"] 

RUN cd /ws_moveit2 \
 && source /opt/ros/jazzy/setup.bash \
 && colcon build --mixin release

RUN apt-get update && apt-get install -y \
      ros-jazzy-rmw-cyclonedds-cpp && \
    rm -rf /var/lib/apt/lists/*

ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

COPY demo.launch.py /root/.

CMD ["bash", "-c", "source /ws_moveit2/install/setup.bash && ros2 launch /root/demo.launch.py"]


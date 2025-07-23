FROM osrf/ros:jazzy-desktop-full

RUN apt-get update && apt-get install -y \
      ros-${ROS_DISTRO}-navigation2 \
      ros-${ROS_DISTRO}-nav2-bringup \
      ros-${ROS_DISTRO}-nav2-minimal-tb* && \
    rm -rf /var/lib/apt/lists/*

ENV TURTLEBOT3_MODEL=waffle

CMD ["ros2", "launch", "nav2_bringup", "tb3_simulation_launch.py", "headless:=False"]


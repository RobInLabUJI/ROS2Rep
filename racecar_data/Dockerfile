FROM osrf/ros:jazzy-desktop-full

RUN mkdir -p /colcon_ws/src

RUN cd /colcon_ws/src \
 && git clone https://github.com/linklab-uva/RACECAR_DATA

RUN cd /colcon_ws/src \
 && apt update \
 && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y \
 && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"] 

RUN cd /colcon_ws \
 && source /opt/ros/jazzy/setup.bash \
 && colcon build

RUN apt-get update && apt-get install -y \
      ros-jazzy-can-msgs && \
    rm -rf /var/lib/apt/lists/*

COPY demo.launch.py .

RUN apt-get update && apt-get install -y \
      unzip && \
    rm -rf /var/lib/apt/lists/*

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
 && unzip awscliv2.zip
 
RUN ./aws/install

CMD ["bash", "-c", "aws s3 cp s3://racecar-dataset/RACECAR-ROS2/S5/M-MULTI-SLOW-KAIST /data/S5/M-MULTI-SLOW-KAIST --recursive --no-sign-request && source /colcon_ws/install/setup.bash && ros2 launch demo.launch.py"]


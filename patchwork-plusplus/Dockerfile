FROM osrf/ros:jazzy-desktop-full

RUN mkdir -p /ros2_ws/src

RUN cd /ros2_ws/src && git clone https://github.com/url-kaist/patchwork-plusplus.git

SHELL ["/bin/bash", "-c"] 

RUN cd /ros2_ws \
 && source /opt/ros/jazzy/setup.bash \
 && colcon build --packages-select patchworkpp

RUN apt-get update && apt-get install -y \
      wget && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://laesze-my.sharepoint.com/:u:/g/personal/herno_o365_sze_hu/Eclwzn42FS9GunGay5LPq-EBA6U1dZseBFNDrr6P0MwB2w?download=1 -O /root/lexus3-2024-04-05-gyor.mcap

COPY demo.launch.py /root/.

CMD ["bash", "-c", "source /ros2_ws/install/setup.bash && ros2 launch /root/demo.launch.py"]


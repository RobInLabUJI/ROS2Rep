FROM osrf/ros:foxy-desktop

RUN git clone https://github.com/borglab/gtsam.git --branch 4.2a8 \
 && cd gtsam && mkdir build && cd build && cmake .. && make install \
 && cd ../.. && rm -fr gtsam

RUN mkdir -p /colcon_ws/src

RUN cd /colcon_ws/src \
 && git clone https://github.com/zhongshp/Co-LRIO.git

SHELL ["/bin/bash", "-c"] 

RUN cd /colcon_ws \
 && source /opt/ros/foxy/setup.bash \
 && colcon build

RUN apt-get update && apt-get install -y \
      wget && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /S3E_Playground_3 && cd /S3E_Playground_3 \
 && wget https://huggingface.co/datasets/PengYu-Team/S3E/resolve/main/S3Ev2/S3E_Playground_3/alpha_gt.txt \
 && wget https://huggingface.co/datasets/PengYu-Team/S3E/resolve/main/S3Ev2/S3E_Playground_3/bob_gt.txt \
 && wget https://huggingface.co/datasets/PengYu-Team/S3E/resolve/main/S3Ev2/S3E_Playground_3/carol_gt.txt \
 && wget https://huggingface.co/datasets/PengYu-Team/S3E/resolve/main/S3Ev2/S3E_Playground_3/metadata.yaml \
 && wget https://huggingface.co/datasets/PengYu-Team/S3E/resolve/main/S3Ev2/S3E_Playground_3/S3E_Playground_3.db3

RUN apt-get update && apt-get install -y \
      ros-foxy-xacro && \
    rm -rf /var/lib/apt/lists/*

COPY demo.launch.py /root/.

CMD ["bash", "-c", "source /colcon_ws/install/setup.bash && ros2 launch /root/demo.launch.py"]


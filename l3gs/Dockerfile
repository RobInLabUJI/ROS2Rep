FROM osrf/ros:humble-desktop-full

SHELL ["/bin/bash", "-i", "-c"]

RUN curl -L -O "https://github.com/conda-forge/miniforge/releases/download/25.3.0-3/Miniforge3-25.3.0-3-Linux-x86_64.sh"

RUN (echo -e "\nyes"; echo -e "\nyes\n")| bash Miniforge3-25.3.0-3-Linux-x86_64.sh

RUN conda install mamba -c conda-forge -y

RUN mamba create -n droid_slam_ros_env python=3.10.12 -y \
 && mamba activate droid_slam_ros_env \
 && python -m pip install --upgrade pip \
 && pip uninstall torch torchvision functorch tinycudann \
 && pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118 \
 && conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit -y \
 && pip install setuptools==69.5.1 # ImportError: cannot import name packaging from pkg_resources  \
 && pip install ninja git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch \
 && pip install nerfstudio

#RUN conda config --env --add channels conda-forge \
# && conda config --env --add channels robostack \
# && conda config --env --add channels robostack-humble \
# && conda config --env --add channels robostack-experimental \
# && mamba install ros-humble-desktop-full # Will fail \
# && conda config --env --add channels conda-forge \
# && conda config --env --add channels robostack-staging \
# && conda config --env --remove channels defaults \
# && mamba install ros-humble-desktop -y \
# && mamba install ros-humble-desktop-full -y \
# && pip install torch-scatter==2.1.1 \
# && pip install matplotlib==3.7.2 \
# && pip install matplotlib-inline==0.1.6


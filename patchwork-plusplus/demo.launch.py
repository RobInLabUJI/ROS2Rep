from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    patchworkpp_launch_file = os.path.join(
        get_package_share_directory('patchworkpp'),
        'launch',
        'patchworkpp.launch.py'
    )
    rosbag_path = '/root/lexus3-2024-04-05-gyor.mcap'
    ld = LaunchDescription()
    patchworkpp_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(patchworkpp_launch_file),
        launch_arguments={
            'visualize': 'true',
            'use_sim_time': 'true',
            'cloud_topic': '/lexus3/os_center/points',
            'base_frame': 'lexus3/os_center_a_laser_data_frame'
        }.items()
    )
    rosbag_play = ExecuteProcess(
        cmd=['ros2', 'bag', 'play', rosbag_path, '--loop'],
        output='screen'
    )
    ld.add_action(patchworkpp_launch)
    ld.add_action(rosbag_play)
    return ld
    

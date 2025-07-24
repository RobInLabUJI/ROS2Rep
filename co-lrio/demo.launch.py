from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    co_lrio_launch_file = os.path.join(
        get_package_share_directory('co_lrio'),
        'launch',
        'run.launch.py'
    )
    rosbag_path = '/S3E_Playground_3'
    ld = LaunchDescription()
    co_lrio_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(co_lrio_launch_file)
    )
    rosbag_play = ExecuteProcess(
        cmd=['ros2', 'bag', 'play', rosbag_path],
        output='screen'
    )
    ld.add_action(co_lrio_launch)
    ld.add_action(rosbag_play)
    return ld
    

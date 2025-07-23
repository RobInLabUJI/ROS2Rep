from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    moveit2_tutorials_dir = get_package_share_directory('moveit2_tutorials')
    
    mtc_demo_launch = os.path.join(moveit2_tutorials_dir, 'launch', 'mtc_demo.launch.py')
    mtc_demo_minimal_launch = os.path.join(moveit2_tutorials_dir, 'launch', 'mtc_demo_minimal.launch.py')

    mtc_demo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(mtc_demo_launch)
    )
    
    mtc_minimal_delayed = TimerAction(
        period=5.0,  # Delay in seconds
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(mtc_minimal_launch)
            )
        ]
    )
    
    return LaunchDescription([
        mtc_demo,
        mtc_minimal_delayed
    ])

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    racecar_utils_pkg = get_package_share_directory('racecar_utils')
    bag_path = os.path.join('data', 'S5', 'M-MULTI-SLOW-KAIST')
    lidar_rviz_config = os.path.join('data', 'lidar_tf.rviz')
    cameras_rviz_config = os.path.join('data', 'cameras.rviz')

    ego_topic = LaunchConfiguration('ego_topic', default='/vehicle_8/local_odometry')
    opp_topic = LaunchConfiguration('opp_topic', default='/vehicle_4/local_odometry')

    odom_to_tf_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(racecar_utils_pkg, 'launch', 'odom_to_tf.launch.py')
        ),
        launch_arguments={
            'ego_topic': ego_topic,
            'opp_topic': opp_topic
        }.items()
    )

    bag_play = ExecuteProcess(
        cmd=['ros2', 'bag', 'play', bag_path],
        output='screen'
    )

    rviz_lidar = ExecuteProcess(
        cmd=['rviz2', '-d', lidar_rviz_config],
        output='screen'
    )

    rviz_cameras = ExecuteProcess(
        cmd=['rviz2', '-d', cameras_rviz_config],
        output='screen'
    )

    return LaunchDescription([
        odom_to_tf_launch,
        bag_play,
        rviz_lidar,
        rviz_cameras
    ])

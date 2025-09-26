from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('arabian_robot')
    urdf_file = os.path.join(pkg_share_dir, 'urdf', 'my_arabian_robot.urdf')

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
    # robot_state_publisher 
    Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    ),

    # joint_state_publisher_gui 
    Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    ),

    Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )
])

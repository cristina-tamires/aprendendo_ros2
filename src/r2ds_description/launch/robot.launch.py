from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    rviz_arg = DeclareLaunchArgument(
        name='rviz_config', default_value=get_package_share_directory('r2ds_description')+'/rviz/robot.rviz',
        description='map used for navigation')

    robot_description = ParameterValue(Command(['xacro ', get_package_share_directory('r2ds_description'), '/urdf/robot.urdf']), value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='log',
        parameters=[{
            'use_sim_time': True,
            'robot_description': robot_description
        }],
        remappings=[
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static')
        ]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='own_log',
        parameters=[{
            'use_sim_time': True
        }],
        arguments=['-d', LaunchConfiguration('rviz_config')]
    )

    teleop = Node(
        name='teleop_twist_keyboard',
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        output='log',
        prefix=["xterm -hold -e"],
        remappings=[
            # ('/cmd_vel', '/demo/cmd_vel'),
        ]
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'R2D2',
            '-topic', 'robot_description'
        ]
    )
   
    return LaunchDescription([
        rviz_arg,
        robot_state_publisher_node,
        spawn_entity,
        rviz_node,
        teleop
    ])

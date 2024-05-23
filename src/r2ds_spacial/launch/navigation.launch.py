from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable

def generate_launch_description():

    map_arg = DeclareLaunchArgument(
        name='map', default_value='')

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('pacote_de_exemplos'), '/launch/simulation.launch.py']),
           launch_arguments={
                'world_path': [get_package_share_directory('pacote_de_exemplos'), '/simulation/worlds/simple_room_with_fixed_boxes.world'],
            }.items(),
    )

    load_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('r2ds_description'),'/launch/robot.launch.py']),
        launch_arguments={
            'rviz_config': [get_package_share_directory('r2ds_spacial'), '/rviz/navigation.rviz'],
        }.items()
   
    )

# -----------------------------------------------------

    bringup_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'),'/launch/bringup_launch.py']),
        launch_arguments={
            'use_namespace': 'False',
            'slam': 'False',
            'map': LaunchConfiguration('map'),
            'use_sim_time': 'True',
            'params_file': [get_package_share_directory('r2ds_spacial'),'/config/navigation.yaml'],
            'autostart': 'True',
            'use_composition': 'True',
            'use_respawn': 'False'
        }.items()
    )


# -----------------------------------------------------

    ld = LaunchDescription()
    ld.add_action(map_arg)
    ld.add_action(simulation)
    ld.add_action(load_robot)
    ld.add_action(bringup_cmd)
    return ld
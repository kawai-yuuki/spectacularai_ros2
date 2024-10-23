from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def launch_setup(context, *args, **kwargs):
    # Spectacular AI ノードを起動
    spectacularai_node = Node(
        package='spectacularai_depthai',  # あなたのパッケージ名
        executable='color_mapping_node',  # 実行可能ファイル名
        parameters=[
            {'recordingFolder': LaunchConfiguration('recordingFolder')},  # パラメータを設定
        ],
        output='screen'
    )

    # RVizノードのオプション起動
    rviz_node = Node(
        condition=IfCondition(LaunchConfiguration("use_rviz")),
        package='rviz2',
        executable='rviz2',
        arguments=['--display-config', 'launch/mapping.rviz'],
        output='screen'
    )

    return [spectacularai_node, rviz_node]


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument('use_rviz', default_value='True', description='RVizを使用するかどうかを指定します'),
            DeclareLaunchArgument('recordingFolder', default_value='', description='録画用のフォルダを指定します')
        ] + [
            OpaqueFunction(function=launch_setup)
        ]
    )

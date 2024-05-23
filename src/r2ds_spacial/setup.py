from setuptools import find_packages, setup

package_name = 'r2ds_spacial'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/cartographer.lua']),
        ('share/' + package_name + '/launch', ['launch/cartographer.launch.py']),
        ('share/' + package_name + '/rviz', ['rviz/cartographer.rviz']),
        ('share/' + package_name + '/config', ['config/navigation.yaml']),
        ('share/' + package_name + '/launch', ['launch/navigation.launch.py']),
        ('share/' + package_name + '/rviz', ['rviz/navigation.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

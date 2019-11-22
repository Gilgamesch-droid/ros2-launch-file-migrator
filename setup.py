from setuptools import setup, find_packages

package_name = "ros2_launch_file_migrator"

setup(
  name=package_name,
  version="0.4",
  description="Migrates a ROS1 XML launch file into a ROS2 Python launch file",
  url="https://github.com/aws-robotics/ros2-launch-file-migrator/",
  author="AWS RoboMaker",
  author_email="ros-contributions@amazon.com",
  maintainer="AWS RoboMaker",
  maintainer_email="ros-contributions@amazon.com",
  keywords=['ROS', 'ROS2'],
  license="Apache License, Version 2.0",
  packages=find_packages(),
  package_data={
    "ros2_launch_file_migrator": ["templates/*"]
  },
  install_requires=[
    'jinja2',
    'autopep8'
  ],
  tests_require=[
    'pytest'
  ],
  scripts=[package_name + "/bin/migrate_launch_file"],
  zip_save=True,
  python_requires='>=3.6'
)
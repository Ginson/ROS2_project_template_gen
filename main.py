import yaml
import subprocess
import os

project_info_data = dict()

def get_package_name()->str:
    return project_info_data['package_name']

def create_ros2_package(package_name:str):
    pass

if __name__ == "__main__":
    project_info_file = "project_info.yaml"
    with open(project_info_file, "r") as project_data:
        project_info_data = yaml.safe_load(project_data)

    # create a ros2 package dir with package name
    pkg_name = get_package_name()
    create_ros2_package(pkg_name)


    
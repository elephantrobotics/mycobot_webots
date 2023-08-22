#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File    : urdf_to_webots.py
# @Author  : Wang Weijian
# @Time    :  2023/08/11 14:09:03
# @function: Convert the urdf model file of the robotic arm to a .proto file supported by webots
# @version : V1

from urdf2webots.importer import convertUrdfFile

# URDF文件路径
urdf_file_path = "./mycobot_pi/mycobot_urdf.urdf"

# 转换为Webots模型,输出的文件格式为.PROTO
converted_model = convertUrdfFile(urdf_file_path)

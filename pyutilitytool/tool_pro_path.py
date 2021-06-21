#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    ：2020/9/23 18:16
@Author  ：维斯
@File    ：tool_pro_path.py
@Version ：1.0
@Function：获取当前项目根路径
"""

import os


def get_project_path(project_name=None, print_log=False):
    """
    获取当前项目根路径
    :param project_name: 项目名称
                            1、可在调用时指定
                            2、[推荐]也可在此方法中直接指定 将'PyUtilityTool'替换为当前项目名称即可（调用时即可直接调用 不用给参数）
    :param print_log: 是否打印日志信息
    :return: 指定项目的根路径
    """
    p_name = 'PyUtilityTool' if project_name is None else project_name
    project_path = os.path.abspath(os.path.dirname(__file__))
    # Windows
    if project_path.find('\\') != -1: separator = '\\'
    # Mac、Linux、Unix
    if project_path.find('/') != -1: separator = '/'

    root_path = project_path[:project_path.find(f'{p_name}{separator}') + len(f'{p_name}{separator}')]
    if print_log: print(f'当前项目名称：{p_name}\r\n当前项目根路径：{root_path}')
    return root_path


if __name__ == '__main__':
    get_project_path()

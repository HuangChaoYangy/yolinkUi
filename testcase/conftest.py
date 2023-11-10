# -*- coding: utf-8 -*-
# @Time    : 2023/11/9 21:48
# @Author  : 黄朝阳
# @FileName: conftest
# @Software: PyCharm

import pytest

# 自动化测试止执行前 -- 环境初始化操作
@pytest.fixture(scope="session",autouse=True)        #function（测试函数级别），class（测试类级别），module（测试模块“.py”级别），session（多个文件级别）。默认是function级别
def start_running():
    print('---马上开始执行自动化测试---')
    yield   # 通过yield来唤醒teardown执行
    print('\n---自动化测试完成,开始处理本次测试数据---')

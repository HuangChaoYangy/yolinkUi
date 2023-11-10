# -*- coding: utf-8 -*-
# @Time    : 2023/11/10 13:23
# @Author  : 黄朝阳
# @FileName: log
# @Software: PyCharm


import logging, time, colorlog, os
from base_dir import log_dir
from logging.handlers import RotatingFileHandler
# from concurrent_log_handler import ConcurrentRotatingFileHandler
# from datetime import timedelta
# import win32com.client

log_colors_config = {
    'DEBUG': 'green',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',}

class Bf_log(object):

    def __init__(self, name):
        self.log = logging.getLogger(name)
        self.log.setLevel('DEBUG')
        self.log.handlers.clear()  # 清除多余的日志，只保留一条
        # self.log = logging.shutdown()   # 可关闭所有记录器，也就使得日志文件被关闭

        log_name = log_dir + "\\" + time.strftime("%Y-%m-%d", time.localtime()) + " all.log"
        # print(log_name)
        if not os.path.exists(log_name):
            with open(log_name, "w", encoding="utf-8")as f:
                f.close()

        # 设置格式
        # fmt = '%(asctime)s-%(filename)s-%(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
        # fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        fmt = '%(log_color)s [%(name)s] [%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        # fmt = "%(asctime)s %(pathname)s %(filename)s %(funcName)s %(lineno)s %(level name)s - %(message)s",
        # "%Y-%m-%d %H:%M:%S"
        # formatter = logging.Formatter(fmt=fmt)
        # formatter = colorlog.ColoredFormatter(fmt=fmt, colorlog=log_colors_config)
        formatter = colorlog.ColoredFormatter(fmt=fmt, log_colors=log_colors_config)  # 日志输出格式
        # 输出渠道
        console_handler = logging.StreamHandler()

        # 配置化
        # 给输出渠道设置日志级别
        console_handler.setLevel("DEBUG")
        # 给输出渠道设置日志格式
        console_handler.setFormatter(formatter)

        # 按照日志文件大小进行切割，超过10M时切割，最多保留10个日志文件
        file_handle = RotatingFileHandler(log_name, maxBytes=1024 * 1024 * 10, backupCount=10, encoding="utf-8", mode="a")
        # file_handle = ConcurrentRotatingFileHandler(log_name, maxBytes=1024 * 100, backupCount=5, encoding="utf-8")

        file_handle.setLevel("DEBUG")
        file_handle.setFormatter(formatter)
        self.log.addHandler(console_handler)
        self.log.addHandler(file_handle)

    def info(self, msg):
        self.log.info(msg)

    def debug(self, msg):
        self.log.debug(msg)

    def error(self, msg):
        self.log.error(msg)

    def critical(self, msg):
        self.log.critical(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def exception(self, msg):
        self.log.exception(msg)



if __name__ == '__main__':

    blog = Bf_log(name='111111111111111111111')
    blog.debug('接口请求错误')
    blog.info(2231321321)
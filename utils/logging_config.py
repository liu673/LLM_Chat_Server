# -*- coding: utf-8 -*-
# Author: Jensen

import datetime
import logging
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
import os

# 日志等级设置
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

# 日志文件路径
LOG_DIR = '../logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
LOG_FILE = os.path.join(LOG_DIR, f'app_{current_date}.log')  # 每天一个日志文件

# 日志格式
LOG_FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

# 日志处理器：基于时间的文件处理器和控制台处理器
LOG_FILE_HANDLER = TimedRotatingFileHandler(LOG_FILE, when='midnight', interval=1, backupCount=5)  # 每天午夜滚动，保留最近5天
# LOG_FILE_HANDLER = RotatingFileHandler(LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=5)  # 文件大小10MB，最多备份5个文件
LOG_CONSOLE_HANDLER = logging.StreamHandler()  # 控制台处理器

LOG_FILE_HANDLER.setLevel(LOG_LEVEL)
LOG_CONSOLE_HANDLER.setLevel(LOG_LEVEL)

LOG_FILE_HANDLER.setFormatter(LOG_FORMATTER)
LOG_CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)

# 日志记录器配置
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(LOG_LEVEL)
LOGGER.addHandler(LOG_FILE_HANDLER)  # 添加文件处理器
LOGGER.addHandler(LOG_CONSOLE_HANDLER)  # 添加控制台处理器


def get_logger(name=None):
    """ 获取logger实例 """
    return LOGGER.getChild(name) if name else LOGGER

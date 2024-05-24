# -*- coding: utf-8 -*-
# Author: Jensen

import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)


class Config:
    # 服务配置
    PORT = int(os.getenv('PORT', 3001))  # 服务端口
    HOST = os.getenv('HOST', '0.0.0.0')  # 默认监听所有接口
    # 模型API URL应当是外部访问Flask应用的地址，如果LLM Server和Flask在同一机器，则可使用localhost
    MODEL_URL = os.getenv("MODEL_URL", f"http://localhost:{PORT}/generate")

    # 模型配置
    MODEL_NAME = os.getenv('MODEL_NAME')
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    MODEL_CACHE = os.path.join(BASE_DIR, os.getenv('MODEL_CACHE'))

    MODEL_PATH = os.getenv('MODEL_PATH', Path(MODEL_CACHE, MODEL_NAME))
    TRUST_REMOTE_CODE = os.getenv('TRUST_REMOTE_CODE', 'True')

    # 日志配置
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
    LOG_DIR = '../logs'

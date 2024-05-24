# -*- coding: utf-8 -*-
# Author: Jensen

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from LLM_Chat_Server.config.base import Config
from modelscope import snapshot_download


# 下载千问1.5-1.8B模型
model_dir = snapshot_download(Config.MODEL_NAME, cache_dir=Config.MODEL_CACHE)


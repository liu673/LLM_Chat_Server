# -*- coding: utf-8 -*-
# Author: Jensen

import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from LLM_Chat_Server.config import Config
from LLM_Chat_Server.app import app
from LLM_Chat_Server.utils import get_logger

logger = get_logger(__name__)


if __name__ == '__main__':
    logger.info("Starting the Flask src...")
    app.run(port=Config.PORT, debug=False, host=Config.HOST)

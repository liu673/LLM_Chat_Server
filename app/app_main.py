# -*- coding: utf-8 -*-
# Author: Jensen

from flask import Flask, request, jsonify
from LLM_Chat_Server.models import ModelSingleton
from LLM_Chat_Server.config import Config
from LLM_Chat_Server.utils import get_logger

app = Flask(__name__)
model_singleton = ModelSingleton.get_instance(Config.MODEL_PATH)  # 应用启动时加载模型
logger = get_logger(__name__)


@app.route("/generate", methods=["POST", "GET"])
def generate():
    data = request.get_json()
    try:
        logger.info("The model is being imported, please wait...")
        response = model_singleton.predict(data)
        logger.info("The model has been imported.")
        status_code = 200
        status_msg = "success"
        logger.info(f"Generated response: {response}")
    except ValueError as ve:
        response = f"Invalid input: {str(ve)}"
        status_code = 400
        status_msg = "bad_request"
        logger.error(response)
    except Exception as e:
        response = f"Internal Server Error: {str(e)}"
        status_code = 500
        status_msg = "error"
        logger.error(response)

    return jsonify({"output": [response], "status": status_msg})


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    logger.info("Starting the Flask src...")
    app.run(port=Config.PORT, debug=False, host=Config.HOST)

# {"message": [{"role": "user", "content": "你能做什么"}], "history": ""}

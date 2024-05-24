# -*- coding: utf-8 -*-
# Author: Jensen
import os
import sys
import asyncio
from httpx import AsyncClient, RequestError, HTTPStatusError
from retrying import retry

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from LLM_Chat_Server.config import Config
from LLM_Chat_Server.utils import get_logger

logger = get_logger(__name__)
client = AsyncClient()


class ModelAPI:
    def __init__(self):
        self.url = Config.MODEL_URL

    async def _send_request(self, data):
        try:
            response = await client.post(self.url, json=data, timeout=30, headers={'Content-Type': 'application/json'})
            response.raise_for_status()
            return response.json()
        except RequestError as exc:
            logger.error(f"Request error: {exc}")
            return {}
        except HTTPStatusError as exc:
            logger.error(f"HTTP error: {exc}")
            return {}

    @retry(stop_max_attempt_number=3, wait_fixed=1000, retry_on_exception=lambda e: isinstance(e, Exception))
    async def chat(self, query, history):
        data = {"message": [{"role": "user", "content": query}], "history": history}
        response_data = await self._send_request(data)
        output = response_data.get("output", [""])
        history = response_data.get("history", [""])
        return output[0], history


async def main():
    model_api = ModelAPI()
    query = "你是谁？"
    history = [""]
    response, history = await model_api.chat(query, history)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())

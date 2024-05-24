# -*- coding: utf-8 -*-
# Author: Jensen

from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
import os


class ModelSingleton:
    _instance = None

    @classmethod
    def get_instance(cls, model_name_path: str) -> 'ModelSingleton':
        if cls._instance is None:
            cls._instance = cls(model_name_path)
        return cls._instance

    def __init__(self, model_name_path: str):
        try:
            trust_remote_code = os.getenv('TRUST_REMOTE_CODE', 'False').lower() == 'true'
            self.tokenizer = AutoTokenizer.from_pretrained(model_name_path, trust_remote_code=trust_remote_code)
            self.model = AutoModelForCausalLM.from_pretrained(model_name_path, trust_remote_code=trust_remote_code,
                                                              device_map="auto")
            self.model.generation_config = GenerationConfig.from_pretrained(model_name_path)
        except Exception as e:
            raise ValueError(f"Failed to load model: {e}")

    def predict(self, data: dict) -> str:
        text = self.tokenizer.apply_chat_template(data["message"], tokenize=False)
        inputs = self.tokenizer([text], return_tensors='pt').to(self.model.device)
        outputs = self.model.generate(inputs.input_ids, max_length=1024)
        generated_ids = [output[len(input_id):] for input_id, output in zip(inputs.input_ids, outputs)]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response

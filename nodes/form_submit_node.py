import os
import json
from aiohttp import web
from server import PromptServer

CATEGORY_NAME = "Form Submit"
CACHE_FILE = os.path.join(os.path.dirname(__file__), "../files/config.sh")


class FormSubmitNode:
    """
    表单提交节点
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "type": (["Doubao","Qwen","OpenAI", "Kimi", "DeepSeek","Claude"],),  
                "api_key": ("STRING",  {"multiline": True}),
                "api_version": ("STRING",  {"multiline": True}),
                "api_base": ("STRING",  {"multiline": True}),
                "api_model": ("STRING",  {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "func"
    OUTPUT_NODE = True
    CATEGORY = CATEGORY_NAME

    def func(self, type, api_key, api_version, api_base, api_model):
        output_text = ""
        print(f"FormSubmitNode: type={type}")
        os.environ["llm_type"] = type
        os.environ["api_key"] = api_key
        os.environ["api_version"] = api_version
        os.environ["api_base"] = api_base
        os.environ["api_model"] = api_model
        print("FormSubmitNode: env-type=",os.environ.get("llm_type"))

        config_content = f"export llm_type={type}\n"
        config_content += f"export api_key={api_key}\n"
        config_content += f"export api_version={api_version}\n"
        config_content += f"export api_base={api_base}\n"
        config_content += f"export api_model={api_model}\n"
        self.save_config(config_content)
        return (output_text,)
    


    def save_config(self,data):
        with open(CACHE_FILE, "w") as f:
            f.write(data)
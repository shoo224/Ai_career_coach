"""
responsible for communicating with gemini api 
"""

from google import genai
from config import config
from typing import Any, Optional

class GeminiService:
    def __init__(self):
        config.validate()

        self.client = genai.Client(
            api_key=config.GEMINI_API_KEY
        )

        self.model = config.MODEL_NAME

    def generate_response(self, prompt:str, generation_config: Optional[Any] = None) -> Any:
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config = generation_config
            )

            return response

        except Exception as e:
            return f"Error generating response: {str(e)}"

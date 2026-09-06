"""
responsible for communicating with gemini api 
"""

from google import genai
from config import config

import google.genai as genai

class GeminiService:
    def __init__(self):
        config.validate()

        self.client = genai.Client(
            api_key=config.GEMINI_API_KEY
        )

        self.model = config.MODEL_NAME

    def generate_response(self, prompt):
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            return response.text

        except Exception as e:
            return f"Error generating response: {str(e)}"

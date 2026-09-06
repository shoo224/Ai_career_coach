from abc import ABC, abstractmethod
from services.gemini_service import GeminiService
from memory.shared_memory import SharedMemory
import config
from google import genai

class BaseAgent(ABC):
    """
    abstart class for all AI agents.

    """

    def __init__(self , memory:SharedMemory) :
        super().__init__()
        self.memory = memory
        self.gemini = GeminiService()

    @abstractmethod
    def execute(self) -> None:
        #execute agent

        pass

    def ask_gemini(self, prompt: str) -> str | None:
    # send prompt to Gemini
        response = self.gemini.models.generate_content(
        model=config.MODEL_NAME,
        contents=prompt
    )

        return response.text
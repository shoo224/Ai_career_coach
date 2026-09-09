from abc import ABC, abstractmethod
from services.gemini_service import GeminiService
from memory.shared_memory import SharedMemory
import config
from google import genai
from models.agent_response import AgentResponse

class BaseAgent(ABC):
    """
    abstart class for all AI agents.

    1. Build Prompt.
    2. Send Prompt to Gemini.
    3. Create AgentResponse.
    4. Store Response in Shared Memory.
    5. Return AgentResponse.

    """

    def __init__(self , memory:SharedMemory, gemini_service: GeminiService) :
        super().__init__()
        self.memory = memory
        self.gemini = gemini_service

    @abstractmethod
    def get_agent_name(self) -> str:
        #returns the name of the agent.

        pass

    @abstractmethod
    def get_memory_key(self) -> str:
        #returns the memory key where the ooutput should be stored.

        pass

    @abstractmethod
    def build_prompt(self) -> str:
        #builds prompt using data available in shared memory.

        pass

    def execute(self) -> AgentResponse:
        """
        Execute the complete Ai agent workflow
        build prompt -> call gemini -> create agentresponse -> store in sharedmemory
        -> return response
        """
        prompt = self.build_prompt()
        gemini_response = self.gemini.generate_response(prompt)
        agent_response = AgentResponse(
            agent_name = self.get_agent_name(),
            output = gemini_response.text
        )

        self.memory.add(
            self.get_memory_key(),
            agent_response
        )

        return agent_response


    def ask_gemini(self, prompt: str) -> str | None:
    # send prompt to Gemini

        return self.gemini.generate_response(prompt)
"""
mainly responsible for managing the execution of ai agents.
"""
from typing import List
from agents.base_agent import BaseAgent
from memory.shared_memory import SharedMemory


class AgentOrchestrator:
    # executes AI agents in sequence.

    def __init__(self , memory : SharedMemory):

        self.memory = memory
        self.agents : List[BaseAgent] = []

    def register(self , agent: BaseAgent) -> None:
        # register agents 

        self.agents.append(agent)

    def execute(self):
        print("\n Starting Multi Agent Workflow.")

        for agent in self.agents:
            print(f" Executing {agent.get_agent_name()} Agent...")
            response = agent.execute()

            print(f"{response.agent_name} Completed successfully...")

        print("Workflow completed.")
        return self.memory.get("reviewer")


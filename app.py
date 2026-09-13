"""
Ai career coach 
entry point of the application

"""

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.reviewer_agent import ReviewerAgent
from agents.writer_agent import WriterAgent

from orchestrator.agent_orchestrator import AgentOrchestrator

from memory.shared_memory import SharedMemory
from services.gemini_service import GeminiService
from memory.conversation_memory import ConversationMemory


def main() -> None:
    gemini_service = GeminiService()
    conversation_memory = ConversationMemory()
    while True:
        print("="*70)
        print("AI CAREER COACH")
        print("="*70)

        user_query = input("Enter your career goal : \n")

        if user_query.lower() == "exit" or user_query.lower() == "bye":
            break
        

        conversation_memory.add_user_message(user_query)

        # Initialised shared components

        memory = SharedMemory()
        

        # Store the user query

        memory.add("user_query",user_query)

        #create agents

        planner = PlannerAgent(memory , gemini_service , conversation_memory)
        researcher = ResearchAgent(memory , gemini_service , conversation_memory)
        writer = WriterAgent(memory , gemini_service , conversation_memory)
        reviewer = ReviewerAgent(memory , gemini_service , conversation_memory)

        orchestrator = AgentOrchestrator(memory , conversation_memory)
        orchestrator.register(planner)
        orchestrator.register(researcher)
        orchestrator.register(writer)
        orchestrator.register(reviewer)

        conversation_memory.display()

        final_response = orchestrator.execute()

        print("="*60)
        print("FINAL ROADMAP")
        print("="*60)
        print(final_response.output)

if __name__ == '__main__':
    main()

"""
Ai career coach 
entry point of the application

"""

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.reviewer_agent import ReviewerAgent
from agents.writer_agent import WriterAgent

from memory.shared_memory import SharedMemory
from services.gemini_service import GeminiService

def main() -> None:
    print("="*70)
    print("AI CAREER COACH")
    print("="*70)

    user_query = input("Enter your career goal : \n")

    # Initialised shared components

    memory = SharedMemory()
    gemini_service = GeminiService()

    # Store the user query

    memory.add("user_query",user_query)

    #create agents

    planner = PlannerAgent(memory , gemini_service)
    researcher = ResearchAgent(memory , gemini_service)
    writer = WriterAgent(memory , gemini_service)
    reviewer = ReviewerAgent(memory , gemini_service)

    print("\n Planning career Roadmap")
    planner.execute()

    print("\n Researching latest technologies")
    researcher.execute()

    print("\n Writing professional roadmap")
    writer.execute()

    print("\n Reviewing final roadmap...")
    reviewer.execute()

    final_response = memory.get("reviewer")

    print("="*60)
    print("FINAL ROADMAP")
    print("="*60)
    print(final_response.output)

if __name__ == '__main__':
    main()

"""
maintains the conversation context history b/w the user and the AI application.
"""

from typing import List

class ConversationMemory:
    # the stored messages are added to the conversation context.

    def __init__(self):

        self.messages: List[str] = []

    def add_user_message(self , message:str) -> None:

        self.messages.append(f"User : {message}")

    def add_ai_message(self , message:str) -> None:

        self.messages.append(f"Ai : {message}")

    def get_context(self) -> str:

        """
        returns the conversation as a string.       
        """

        return "\n".join(self.messages)

    def clear(self) -> None:
        self.messages.clear()

    def display(self) -> None:
        print("\n"+ "="*60)
        print("CONVERSATION HISTORY")
        print("="*60)

        if not self.messages:
            print("No History Found!!!")
        else:
            for message in self.messages:
                print(message)

        print("=" * 60)


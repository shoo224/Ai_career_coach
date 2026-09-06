"""
Shared memory
acts as a common storage for all agents 
"""
class SharedMemory:
    """
    shared memory accessible by every agent
    """

    def __init__(self):
        self.memory = {}

    def add(self, key: str, value:str) -> None:
        #storing data

        self._memory[key] = value
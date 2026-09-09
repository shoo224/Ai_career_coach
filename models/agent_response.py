"""
Agent Response Model
represents the standardized response by every AI agent.

"""

from dataclasses import dataclass , field
from datetime import datetime
from typing import Optional

@dataclass
class AgentResponse:
    """
    standard response returned by every AI agent
   
    """
    #Name of the Agent
    agent_name  : str
    output : str
    status : str = "SUCCESS"
    error : Optional[str] = None
    timestamp : datetime = field(
        default_factory=datetime.now
    )

    def is_success(self) -> bool:
        #return true if execution was successful.
        return self.status.upper() == "SUCCESS"

    def __str__(self):
        #pretty string representation

        return (
            f"\nAgent : {self.agent_name}"
            f"\nStatus : {self.status}"
            f"\nTimeStamp : {self.timestamp}"
            f"\nError : {self.error}"
        )

    

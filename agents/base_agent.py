from abc import ABC, abstractmethod

from models.pipeline_state import PipelineState


class BaseAgent(ABC):

    @abstractmethod
    def execute(self, state: PipelineState) -> PipelineState:
        """Execute the agent."""
        pass
import os

from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState


class QualityCheckerAgent(BaseAgent):

    def execute(self, state: PipelineState):

        if not state.output_video:
            state.logs.append("Quality Check Failed : No output video")
            return state

        if not os.path.exists(state.output_video):
            state.logs.append("Quality Check Failed : Video file missing")
            return state

        size = os.path.getsize(state.output_video)

        if size == 0:
            state.logs.append("Quality Check Failed : Empty video")
            return state

        state.logs.append("Quality Check Passed")

        return state
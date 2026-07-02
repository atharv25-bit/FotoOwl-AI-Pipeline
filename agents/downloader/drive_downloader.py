from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState


class DriveDownloaderAgent(BaseAgent):

    def execute(self, state: PipelineState):

        print("\nDrive Downloader Agent")

        print("Manual Mode Enabled")
        print("Place all images inside the 'input' folder before running the pipeline.\n")

        state.logs.append("Drive Downloader Ready (Manual Mode)")

        return state
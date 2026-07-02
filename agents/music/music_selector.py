from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState


class MusicSelectorAgent(BaseAgent):

    def execute(self, state: PipelineState):

        storyboard = ""

        if state.storyboard:
            storyboard = state.storyboard[0].lower()

        if "wedding" in storyboard:
            state.music_path = "assets/music/wedding.mp3"

        elif "birthday" in storyboard:
            state.music_path = "assets/music/happy.mp3"

        elif "party" in storyboard:
            state.music_path = "assets/music/party.mp3"

        else:
            state.music_path = "assets/music/cinematic.mp3"

        state.logs.append("Music Selected")

        return state
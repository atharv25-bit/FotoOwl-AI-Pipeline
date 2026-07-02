from langgraph.graph import StateGraph, END

from models.pipeline_state import PipelineState

from agents.downloader.drive_downloader import DriveDownloaderAgent
from agents.loader.image_loader import ImageLoaderAgent
from agents.selector.photo_selector import PhotoSelectorAgent
from agents.analyzer.image_analyzer import ImageAnalyzerAgent
from agents.storyboard.storyboard_agent import StoryboardAgent
from agents.music.music_selector import MusicSelectorAgent
from agents.video.video_composer import VideoComposerAgent
from agents.quality.quality_checker import QualityCheckerAgent


downloader = DriveDownloaderAgent()
loader = ImageLoaderAgent()
selector = PhotoSelectorAgent()
analyzer = ImageAnalyzerAgent()
storyboard = StoryboardAgent()
music = MusicSelectorAgent()
video = VideoComposerAgent()
quality = QualityCheckerAgent()


def download_node(state):
    return downloader.execute(state)


def load_node(state):
    return loader.execute(state)


def selector_node(state):
    return selector.execute(state)


def analyzer_node(state):
    return analyzer.execute(state)


def storyboard_node(state):
    return storyboard.execute(state)


def music_node(state):
    return music.execute(state)


def video_node(state):
    return video.execute(state)


def quality_node(state):
    return quality.execute(state)


def build_workflow():

    workflow = StateGraph(PipelineState)

    workflow.add_node("download", download_node)
    workflow.add_node("load", load_node)
    workflow.add_node("selector", selector_node)
    workflow.add_node("analyzer", analyzer_node)
    workflow.add_node("storyboard", storyboard_node)
    workflow.add_node("music", music_node)
    workflow.add_node("video", video_node)
    workflow.add_node("quality", quality_node)

    workflow.set_entry_point("download")

    workflow.add_edge("download", "load")
    workflow.add_edge("load", "selector")
    workflow.add_edge("selector", "analyzer")
    workflow.add_edge("analyzer", "storyboard")
    workflow.add_edge("storyboard", "music")
    workflow.add_edge("music", "video")
    workflow.add_edge("video", "quality")
    workflow.add_edge("quality", END)

    return workflow.compile()
from graph.workflow import build_workflow
from models.pipeline_state import PipelineState


graph = build_workflow()

result = graph.invoke(PipelineState())

print("\n========== PIPELINE LOGS ==========\n")

for log in result["logs"]:
    print(log)

print("\nOutput Video")
print(result["output_video"])

print("\nMusic")
print(result["music_path"])
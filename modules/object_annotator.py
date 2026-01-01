from .base import LlamaClient, console
from rich.panel import Panel

class ObjectAnnotator:
    def __init__(self):
        self.client = LlamaClient()
    
    def annotate(self, object_name: str, context: str) -> str:
        console.print(Panel(f"🏷️ Annotating: {object_name}", style="cyan"))
        prompt = f"""Create AR annotations for: {object_name}

Context: {context}

Generate:
1. Object identification text
2. Key information points
3. Technical specifications
4. Historical/contextual info
5. Interactive hotspots
6. Related object connections"""
        return self.client.generate(prompt)

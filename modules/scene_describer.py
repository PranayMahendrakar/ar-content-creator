from .base import LlamaClient, console
from rich.panel import Panel

class SceneDescriber:
    def __init__(self):
        self.client = LlamaClient()
    
    def describe(self, scene: str, detail_level: str = "medium") -> str:
        console.print(Panel("📸 Describing Scene", style="yellow"))
        prompt = f"""Create AR scene description:

Scene: {scene}
Detail Level: {detail_level}

Provide:
1. Spatial layout
2. Key objects and positions
3. Atmospheric elements
4. Points of interest
5. Navigation markers
6. AR overlay opportunities"""
        return self.client.generate(prompt)

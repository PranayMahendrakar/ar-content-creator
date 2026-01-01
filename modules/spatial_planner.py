from .base import LlamaClient, console
from rich.panel import Panel

class SpatialPlanner:
    def __init__(self):
        self.client = LlamaClient()
    
    def plan(self, space_description: str, content_elements: list) -> str:
        console.print(Panel("📐 Planning Spatial Layout", style="green"))
        elements = ", ".join(content_elements)
        prompt = f"""Plan AR spatial layout:

Space: {space_description}
Elements: {elements}

Design:
1. Content positioning
2. Depth layering
3. Field of view optimization
4. Occlusion handling
5. Scale adjustments
6. Movement paths"""
        return self.client.generate(prompt)

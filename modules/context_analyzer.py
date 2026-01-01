from .base import LlamaClient, console
from rich.panel import Panel

class ContextAnalyzer:
    def __init__(self):
        self.client = LlamaClient()
    
    def analyze(self, scene_description: str, ar_purpose: str) -> str:
        console.print(Panel("🔍 Analyzing Context", style="blue"))
        prompt = f"""Analyze AR context:

Scene: {scene_description}
Purpose: {ar_purpose}

Determine:
1. Key environmental elements
2. Interaction opportunities
3. Lighting considerations
4. Scale factors
5. User perspective points
6. Content placement zones"""
        return self.client.generate(prompt)

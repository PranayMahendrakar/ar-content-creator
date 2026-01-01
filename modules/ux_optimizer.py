from .base import LlamaClient, console
from rich.panel import Panel

class UXOptimizer:
    def __init__(self):
        self.client = LlamaClient()
    
    def optimize(self, ar_experience: str) -> str:
        console.print(Panel("⚡ Optimizing UX", style="yellow"))
        prompt = f"""Optimize AR user experience:

Experience: {ar_experience}

Improve:
1. Load time optimization
2. Intuitive controls
3. Information clarity
4. Cognitive load reduction
5. Accessibility features
6. Error prevention"""
        return self.client.generate(prompt)

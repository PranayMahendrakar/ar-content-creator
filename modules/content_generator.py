from .base import LlamaClient, console
from rich.panel import Panel

class ContentGenerator:
    def __init__(self):
        self.client = LlamaClient()
    
    def generate(self, context: str, content_type: str, target_audience: str) -> str:
        console.print(Panel("✨ Generating AR Content", style="green"))
        prompt = f"""Generate AR content:

Context: {context}
Type: {content_type}
Audience: {target_audience}

Create:
1. Content description
2. Visual elements
3. Text overlays
4. Information hierarchy
5. Engagement hooks
6. Call-to-action elements"""
        return self.client.generate(prompt)

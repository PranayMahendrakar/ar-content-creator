from .base import LlamaClient, console
from rich.panel import Panel

class AnimationDirector:
    def __init__(self):
        self.client = LlamaClient()
    
    def direct(self, element: str, animation_purpose: str) -> str:
        console.print(Panel("🎬 Directing Animation", style="red"))
        prompt = f"""Direct AR animation:

Element: {element}
Purpose: {animation_purpose}

Specify:
1. Animation type
2. Timing/duration
3. Easing curves
4. Loop behavior
5. Trigger conditions
6. Performance optimization"""
        return self.client.generate(prompt)

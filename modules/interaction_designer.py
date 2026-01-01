from .base import LlamaClient, console
from rich.panel import Panel

class InteractionDesigner:
    def __init__(self):
        self.client = LlamaClient()
    
    def design(self, ar_experience: str, interaction_type: str) -> str:
        console.print(Panel("👆 Designing Interactions", style="magenta"))
        prompt = f"""Design AR interactions:

Experience: {ar_experience}
Interaction Type: {interaction_type}

Create:
1. Gesture controls
2. Voice commands
3. Gaze-based triggers
4. Touch interactions
5. Proximity triggers
6. Feedback mechanisms"""
        return self.client.generate(prompt)

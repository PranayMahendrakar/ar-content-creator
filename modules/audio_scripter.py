from .base import LlamaClient, console
from rich.panel import Panel

class AudioScripter:
    def __init__(self):
        self.client = LlamaClient()
    
    def script(self, content: str, style: str = "informative") -> str:
        console.print(Panel("🔊 Creating Audio Script", style="blue"))
        prompt = f"""Create AR audio script:

Content: {content}
Style: {style}

Generate:
1. Narration script
2. Sound effect cues
3. Spatial audio placement
4. Timing markers
5. Ambient sounds
6. Interactive audio triggers"""
        return self.client.generate(prompt)

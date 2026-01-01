import requests, json
from rich.console import Console
console = Console()

class LlamaClient:
    def __init__(self, model="llama3.2"):
        self.model = model
    
    def generate(self, prompt: str, system: str = None, stream: bool = True) -> str:
        payload = {"model": self.model, "prompt": prompt, "stream": stream}
        if system: payload["system"] = system
        
        if stream:
            response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
            result = ""
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line).get("response", "")
                    print(chunk, end="", flush=True)
                    result += chunk
            print()
            return result
        return requests.post("http://localhost:11434/api/generate", json=payload).json().get("response", "")

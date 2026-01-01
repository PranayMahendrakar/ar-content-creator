from .base import console
from datetime import datetime
import json

class ExportManager:
    def export(self, ar_project: dict, format: str = "json") -> str:
        console.print(f"[green]💾 Exporting as {format}[/green]")
        filename = f"ar_content_{datetime.now().strftime('%Y%m%d')}.{format}"
        
        with open(filename, "w") as f:
            if format == "json":
                json.dump(ar_project, f, indent=2)
            else:
                for k, v in ar_project.items():
                    f.write(f"# {k}\n{v}\n\n")
        
        return f"Exported to {filename}"

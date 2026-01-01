#!/usr/bin/env python3
"""
Augmented Reality Content Creator
Generates contextual content for AR applications.
Author: Pranay M
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from modules import *

console = Console()

def main():
    console.print(Panel.fit(
        "[bold magenta]🥽 AR Content Creator[/bold magenta]\n"
        "[dim]Create immersive AR experiences[/dim]",
        border_style="magenta"
    ))
    
    context = ContextAnalyzer()
    content = ContentGenerator()
    annotator = ObjectAnnotator()
    scene = SceneDescriber()
    interaction = InteractionDesigner()
    audio = AudioScripter()
    spatial = SpatialPlanner()
    animation = AnimationDirector()
    ux = UXOptimizer()
    export = ExportManager()
    
    project = {}
    
    console.print("\n[yellow]Let's create AR content![/yellow]\n")
    
    scene_desc = Prompt.ask("Describe the scene/environment")
    purpose = Prompt.ask("AR purpose (education, marketing, gaming, etc.)")
    audience = Prompt.ask("Target audience")
    
    project["context"] = context.analyze(scene_desc, purpose)
    project["scene"] = scene.describe(scene_desc)
    project["content"] = content.generate(scene_desc, purpose, audience)
    project["interactions"] = interaction.design(purpose, "touch and gesture")
    project["audio"] = audio.script(purpose)
    project["ux"] = ux.optimize(purpose)
    
    export.export(project)
    console.print("\n[green]✅ AR content created![/green]")

if __name__ == "__main__":
    main()

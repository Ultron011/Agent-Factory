import yaml
from rich.console import Console
from rich.theme import Theme

# Global console with custom styling
theme = Theme({"info": "dim cyan", "warning": "bold yellow", "success": "bold green", "agent": "magenta"})
console = Console(theme=theme)

def load_config(filename: str):
    with open(f"config/{filename}", "r") as f:
        return yaml.safe_load(f)
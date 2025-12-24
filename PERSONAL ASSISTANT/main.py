import os
from dotenv import load_dotenv
from rich.panel import Panel
from rich.live import Live
from rich.status import Status
from src.agents.supervisor_agent import supervisor_agent
from src.utils import console, load_config

config = {"configurable": {'thread_id': '123'}}

load_dotenv()

def run_app():
    console.print(Panel("[bold green]Nexus GenAI Production Environment[/bold green]", expand=False))
    
    while True:
        user_input = console.input("\n[bold cyan]User:[/bold cyan] ")
        if user_input.lower() in ["exit", "quit"]: break

        with Status("[info]Agent is thinking...", console=console) as status:
            config = {"recursion_limit": 20}
            inputs = {"messages": [("user", user_input)]}
            
            # Streaming the graph steps for visibility
            for event in supervisor_agent.stream(inputs, config=config):
                for node, data in event.items():
                    console.print(f"[agent]Active Node:[/agent] [yellow]{node}[/yellow]")
            
            # Retrieve the final response
            final_state = supervisor_agent.get_state(config).values
            last_msg = final_state["messages"][-1].content
            
        console.print(Panel(last_msg, title="[bold green]Assistant[/bold green]", border_style="green"))

if __name__ == "__main__":
    run_app()
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from src.utils import load_config
from src.tools.supervisor_agent_tools import schedule_event, manage_email
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv()

cfg = load_config('settings.yaml')
prompts = load_config('prompts.yaml')

model = init_chat_model(model=cfg["model_settings"]['primary'])

supervisor_agent = create_agent(
    model,
    tools=[schedule_event, manage_email],
    system_prompt=prompts["supervisor_agent"]["system_prompt"],
    checkpointer=InMemorySaver()
)

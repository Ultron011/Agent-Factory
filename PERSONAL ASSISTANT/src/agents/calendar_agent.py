from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from src.utils import load_config
from src.tools.calendar_agent_tools import create_calendar_event, get_available_time_slots
from dotenv import load_dotenv

load_dotenv()

cfg = load_config('settings.yaml')
prompts = load_config('prompts.yaml')

model = init_chat_model(model=cfg["model_settings"]['worker'])

calendar_agent = create_agent(
    model,
    tools=[create_calendar_event, get_available_time_slots],
    system_prompt=prompts["calendar_agent"]["system_prompt"]
)

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from src.utils import load_config
from src.tools.email_agent_tools import send_email
from dotenv import load_dotenv

load_dotenv()

cfg = load_config('settings.yaml')
prompts = load_config('prompts.yaml')

model = init_chat_model(model=cfg["model_settings"]['worker'])

email_agent = create_agent(
    model,
    tools=[send_email],
    system_prompt=prompts["email_agent"]["system_prompt"]
)

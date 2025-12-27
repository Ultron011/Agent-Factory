from datetime import datetime
from market_research_crew.crew import MarketResearchCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'An AI Powered Application for accelerating learning using documentations, research papers and other resources all in one place',
        'current_year': str(datetime.now().year)
    }

    try:
        MarketResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
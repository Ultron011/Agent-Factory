from crewai import Crew, Agent, Task, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool
from typing import List
from dotenv import load_dotenv
load_dotenv()

web_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()
selenium_scraping_tool = SeleniumScrapingTool()

toolkit = [web_search_tool, web_scraping_tool, selenium_scraping_tool]

@CrewBase
class MarketResearchCrew():
    
    agents = List[Agent]
    tasks = List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['market_research_specialist'],
            tools=toolkit
        )
    
    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitive_intelligence_analyst'],
            tools=toolkit
        )
    
    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_insights_researcher'],
            tools=toolkit
        )
    
    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['product_strategy_advisor'],
            tools=toolkit
        )
    
    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['business_analyst'],
            tools=toolkit
        )

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_research_task']
        )
        
    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitive_intelligence_task'],
            context=[self.market_research_task()]
        )

    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['customer_insights_task'],
            context=[self.market_research_task(), self.competitive_intelligence_task()]
        )

    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_strategy_task'],
            context=[self.market_research_task(), self.competitive_intelligence_task(), self.customer_insights_task()]
        )

    @task
    def business_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_analysis_task'],
            context=[self.market_research_task(), self.competitive_intelligence_task(), self.customer_insights_task(), self.product_strategy_task()],
            output_file="reports/report.md"
        )

    @crew 
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
from crewai import Crew, Process
from agents import research_agent
from tasks import research_task
from dotenv import load_dotenv
load_dotenv()


crew = Crew(
    description="A crew dedicated to conducting research and providing summaries of findings.",
    agents=[research_agent],
    tasks=[research_task],
    verbose=True
)


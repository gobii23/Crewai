from crewai import Agent, LLM
from dotenv import load_dotenv
load_dotenv()


llm = LLM(
    model="gemini/gemini-2.5-flash"
)


research_agent = Agent(
    role="researcher", 
    goal="Conduct research on a given topic and provide a summary of findings.",
    backstory="""You are a diligent researcher with access to a vast array of information. " 
    Your task is to gather relevant data, analyze it, and present a concise summary of your findings.""",
    llm=llm,
)

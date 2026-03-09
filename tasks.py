from crewai import Task
from agents import research_agent
import os 
from crewai_tools import SerperDevTool

user_input = input("Enter a research topic: ")
output_location = os.path.join(os.getcwd(), "research_summary.md")



research_task = Task(
    description=f"""Conduct research on the topic: {user_input} and provide a summary of findings and save it in the {output_location}.""",
    expected_output= "Summary of research findings on the given topic as a markdown formatted document.",
    tools=[SerperDevTool()],
    agent=research_agent
)
from crewai import Crew, Process
from agents import layer_one, researcher
from tasks import layer_one_task

# Forming the Blackpink-focused crew with the updated agents and tasks
crew = Crew(
    agents=[layer_one, researcher],
    tasks=[layer_one_task],
    process=Process.sequential,
    memory=True
)

# Starting the task execution process with enhanced feedback
prompt = input("Enter the prompt: ")
result = crew.kickoff(inputs={'prompt': prompt})
print(result)

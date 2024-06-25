from crewai import Crew, Process
from agents import delegator_agent, chore_agent, bug_agent, feature_agent, support_agent
from tasks import notion_helper_task

# Forming the Blackpink-focused crew with the updated agents and tasks
crew = Crew(
    agents=[delegator_agent, chore_agent, bug_agent, feature_agent, support_agent],
    tasks=[notion_helper_task],
    process=Process.sequential,
    memory=True
)

# Starting the task execution process with enhanced feedback
prompt = input("Enter the prompt: ")
result = crew.kickoff(inputs={'user_input': prompt})
print(result)

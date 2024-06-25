from datetime import datetime, timedelta
from crewai import Task
from agents import delegator_agent

# Calculate date range (from today to one month ago)
today = datetime.today().strftime('%Y-%m-%d')
one_month_ago = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
date_range = f"from {one_month_ago} to {today}"

notion_helper_task = Task(
        description="Process the following user input and fill out the appropriate template: {user_input}",
        expected_output="Only return the filled-out template",
        agent=delegator_agent,
        output_file='Layer_one_answer.md'
    )
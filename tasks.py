from datetime import datetime, timedelta
from crewai import Task
from agents import layer_one

# Calculate date range (from today to one month ago)
today = datetime.today().strftime('%Y-%m-%d')
one_month_ago = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
date_range = f"from {one_month_ago} to {today}"

layer_one_task = Task(
    description=(
        "You are the first layer of a team that is responsible for answering this prompt: {prompt}. "
        f"Today's date is {today}. Ensure all information provided is up-to-date and relevant. "
    ),
    expected_output=(
        "A comprehensive answer that includes all the relevant information related to the prompt. The answer should be well-structured and easy to read and include URLs to the sources used to gather information. "
    ),
    agent=layer_one,
    output_file='Layer_one_answer.md'
)
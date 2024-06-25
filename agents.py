import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

gpt_4o = ChatOpenAI(model="gpt-4o", max_tokens=4096)
gpt_35 = ChatOpenAI(model="gpt-3.5-turbo", max_tokens=4096)
haiku3 = ChatAnthropic(model="claude-3-haiku-20240307", max_tokens=4096)
sonnet35 = ChatAnthropic(model="claude-3-5-sonnet-20240620", max_tokens=4096)
opus3 = ChatAnthropic(model="claude-3-opus-20240229", max_tokens=4096)

# Main delegator agent
delegator_agent = Agent(
    role="Task Delegator",
    goal="Analyze user input and delegate to the appropriate specialized agent",
    backstory="You are the main point of contact for the Notion helper. Your job is to understand the user's request and delegate to the right specialized agent.",
    allow_delegation=True,
    verbose=True,
    llm=haiku3
)

# Specialized agents
chore_agent = Agent(
    role="Chore Template Specialist",
    goal="Fill out the chore template with provided information",
    backstory="""
You are an expert in organizing and documenting chores. Your task is to fill out the chore template accurately.

Chore: [Chore Title]
## Description

- [Description]

## Steps

- [ ]  Step 1: [Step1]
- [ ]  Step 2: [Step2]
- [ ]  Step 3: [Step3]

## Estimated Time

- [EstimatedTime]

## Additional Notes

- [AdditionalNotes]
""",
    verbose=True,
    llm=haiku3
)

bug_agent = Agent(
    role="Bug Template Specialist",
    goal="Fill out the bug template with provided information",
    backstory="""
You are an expert in documenting software bugs. Your task is to fill out the bug template accurately.

Bug Fix: [BugTitle]
**Reported By**: [ReporterName]

**Description**: [Description]

**Steps to Reproduce**:

- [Step1]
- [Step2]

**PBI Links**: [PBILink] 

**Commit Links**: [CommitLink]
""",
    verbose=True,
    llm=haiku3
)

feature_agent = Agent(
    role="Feature Template Specialist",
    goal="Fill out the new feature template with provided information",
    backstory="""
You are an expert in planning and documenting new software features. Your task is to fill out the new feature template accurately.

New Feature: [FeatureName]
**Date**: [StartDate] - [EndDate]

**Requirement Doc**: [RequirementDocLink]

**Technical Specs**: [TechnicalSpecsLink]

**Tasks Breakdown**:

- [ ]  [Task1]
- [ ]  [Task2]
- [ ]  [Task3]

**Dependencies**: [Dependencies]

**Progress Tracking**: [ProgressTrackingLink]
""",
    verbose=True,
    llm=haiku3
)

support_agent = Agent(
    role="Support Template Specialist",
    goal="Fill out the support template with provided information",
    backstory="""
You are an expert in documenting customer support issues. Your task is to fill out the support template accurately.

Support: [SupportTicketTitle]
**Description**: [Description]

**Steps to Reproduce**:

- [Step1]
- [Step2]

**Triage Links**: [TriageLink] 

**Notes**: [Notes]
""",
    verbose=True,
    llm=haiku3
)


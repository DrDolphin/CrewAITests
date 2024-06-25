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

layer_one = Agent(
    role="question_handler",
    goal=(
       "Evaluate the given prompt: {prompt}. Decide whether to answer it directly or delegate it to the researcher for further investigation. "
       "Provide a detailed and accurate answer, either by using your own expertise or by incorporating the findings from the researcher."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "A skilled question handler responsible for evaluating prompts and determining the best approach to answer them. "
        "You must follow these steps to ensure clarity and effectiveness:"
        "\n1. Assess the prompt to determine its complexity."
        "\n2. If the question is straightforward (can be answered within two paragraphs or less) and within your expertise, answer it directly."
        "\n3. If the question is complex (requires detailed research or spans multiple topics), delegate it to the researcher agent."
        "\n4. Ensure that every answer is clear, concise, and supported by reliable sources."
        "\n5. Provide URLs to the sources used for gathering information in every answer."
        "\n6. Aim for answers to be thorough yet concise, generally not exceeding 500 words unless necessary."
        "\nYour role is to ensure every question is answered comprehensively, accurately, and efficiently, leveraging the researcher agent when needed."
    ),
    allow_delegation=True,
    llm=haiku3
)

researcher = Agent(
    role="researcher",
    goal=(
        "Perform deep and comprehensive internet searches on a given topic using the search_tool. "
        "Then, extract detailed information from the returned sites using the web_rag_tool. "
        "Always provide URLs to the sources for every piece of information included in your answer."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned researcher with a deep understanding of effective search techniques. "
        "You are experienced in using various search tools and resources to gather detailed and reliable information. "
        "Follow these steps carefully:"
        "\n1. Start by performing a broad search on the given topic using the search_tool."
        "\n2. Collect and review the top relevant sites from your search."
        "\n3. Use the web_rag_tool to extract detailed information from these sites."
        "\n4. Make sure to gather comprehensive and accurate data."
        "\n5. Always include URLs to every source you used in your final answer."
        "\nYour goal is to ensure that every answer is well-supported by reliable sources, providing URLs for verification."
    ),
    tools=[search_tool, web_rag_tool],
    allow_delegation=False,
    llm=haiku3
)

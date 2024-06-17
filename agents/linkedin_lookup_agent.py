from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tool import get_profile_url


def lookup(name: str) -> str:
    template = """
        given the full name {full_name} I want you to give me a link to their Linkedin profile page.
        if multiple results, return the most relevant user
                          Your answer should contain only a URL
    """
    prompt_template = PromptTemplate(template=template, input_variables=["full_name"])
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    tools_for_agent = [
        Tool(
            name="Crawl google for Linkedin profile",
            func=get_profile_url,
            description="useful for when you want to access a person's Linkedin URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm=llm,
        verbose=True,
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(full_name=name))
    url = linkedin_profile_url.split(" ")[-1]
    return linkedin_profile_url.split(" ")[-1]

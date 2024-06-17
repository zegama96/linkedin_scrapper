import os
from langchain import PromptTemplate  # prompt we'll use
from langchain.chat_models import ChatOpenAI  # llm model we'll use
from langchain.chains import (
    LLMChain,
)  # allow us to combine multiple components together and build one single coherent application
from third_parties.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv
from agents.linkedin_lookup_agent import lookup
from output_parsers import person_intel_parser, PersonIntel
from typing import Tuple, List

load_dotenv()


def linkedin_chain(name: str) -> Tuple[PersonIntel, str]:
    summary_template = """
            given the Linkedin information {information} about a person I want you to create:
            1. a short summary
            2. two interesting facts about them 
            3. two topics of interest of that person 
            4. two ice breakers to start a conversation with them   
            \n{format_instructions}
            
    """
    # {} sings a parameter into the prompt template

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )
    llm = ChatOpenAI(
        temperature=0, model_name="gpt-3.5-turbo"
    )  # temperature will decide how creative the language model will be

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    #linkedin_profile_url = lookup(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="")

    print(chain.run(information=linkedin_data))
    result = chain.run(information=linkedin_data)
    person_intel = person_intel_parser.parse(result)
    print("linkedin_data", linkedin_data)
    print("person_intel", person_intel)
    print("person_intel", person_intel.to_dict())

    return (
        person_intel,
        linkedin_data.get("profile_pic_url")
    )


if __name__ == "__main__":
    linkedin_chain("Eden Marco")

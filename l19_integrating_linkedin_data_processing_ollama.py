



from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

from agents import linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

import os
from dotenv import load_dotenv

load_dotenv()

def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent.lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=True)

    summary_template = """
        given the Linkedin {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    #llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    llm = ChatOllama(temperature=0, model="llama3.2_32k")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": linkedin_data})

    print(res)

if __name__ == "__main__":
    
    print("Ice breaker Enter")

    ice_break_with(name="Eden Marco")

    

    

   
    
    

    

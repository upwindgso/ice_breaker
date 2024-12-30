
from typing import Tuple

from output_parsers import summary_parser, Summary

from langchain.output_parsers import format_instructions
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import ChatOllama

from agents import linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

import os
from dotenv import load_dotenv

load_dotenv()

def ice_break_with(name: str, location: str = "", keywords: str = "", mock: bool = True) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent.lookup(name=name, location = location, keywords=keywords)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=mock)

    summary_template = """
        given the Linkedin {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them relevant to a sales pitch about startup business operations consulting

        Use information from linkedin
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template,
        partial_variables={"format_instructions":summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    #llm = ChatAnthropic(temperature=0.1, model='claude-3-5-haiku-latest')
    #llm = ChatOllama(temperature=0, model="llama3.2_32k")

    chain = summary_prompt_template | llm | summary_parser #| StrOutputParser()

    res: Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("profile_pic_url")

if __name__ == "__main__":
    
    print("Ice breaker Enter")

    print(ice_break_with(name="Tim Jones", location="Melbourne", keywords="upwind", mock=True))
    #ice_break_with(name="Cheryl Chen", location="Melbourne", keywords="rev ops", mock=False)

    

    

   
    
    

    

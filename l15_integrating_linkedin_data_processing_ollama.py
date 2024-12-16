



from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile

import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("Hello world")

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

    linedin_data = scrape_linkedin_profile(
        linkedin_profile_url=os.getenv("MY_LINKEDIN_PROFILE"),mock=True
        )
    
    res = chain.invoke(input={"information": linedin_data})

    print(res)

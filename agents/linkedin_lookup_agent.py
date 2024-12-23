import sys
import os

# Add the project root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama


load_dotenv()

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub

from tools.tools import get_profile_url_tavily, get_profile_url_searxng

from langchain_community.tools import HumanInputRun


def lookup(name: str, keywords: str) -> str:
    llm = ChatOpenAI(temperature=0,model="gpt-4o-mini")
    #llm = ChatOllama(temperature=0, model="llama3.2_32k")

    template = """Given the fullname <{name_of_person}> and keywords <{keywords}>,  I want you to get me a link to their LinkedIn profile page.
                    Your answer should contain only a valid linkedin profile url containing 'linkedin.com/in/'.
                    Because you are searching for linkedin profiles, you will send to append your initial searches with the domain 'site:linkedin.com/in/' to help limit relevant results.
                    You will never repeat the same search query because it is wasteful and unnessesary.
                    You make use of the rerank_score information to help sort relevance but still excercise your own judgement and validation. For instance, if several results have a high but similar score, you will not blindly choose the highest score but perform validation yourself.
                    Before answering you will ensure that the 'link' you have selected from the json corresponds the the profile that you intended to select; sometimes you can default to chosing the first link as your final answer when you intended another one from your validation.
    """

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person", "keywords"]

    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            #func=get_profile_url_tavily,
            func=get_profile_url_searxng,
            description="useful for when you need to get the linkein page URL. The reranking_score gives an expert opinion on relevance of the search result."
        )
        #,HumanInputRun(
        #description="Useful when you need to ask a human for help or verification. The input should be a question for the human including what you know and where you are stuck. You will use the information provided by the user to identify new search paths"
        #)
        
    ]


    react_prompt = hub.pull("hwchase17/react")  #default useful prompt for implementing the ReAct paper and CoT promp

    agent = create_react_agent(llm=llm, 
                               tools=tools_for_agent,
                               prompt=react_prompt
                               ) #hold all the ways we cant to communicate/parse with llm and tools  => the recipe
    
    agent_executor = AgentExecutor(agent=agent,
                                   tools=tools_for_agent, 
                                   verbose=True,
                                   handle_parsing_errors=True,
                                   max_iterations=10  # Limit iterations to prevent infinite loops
                                   ) #the runtime that contains all the loops etc => the orchestration

    if name != None: 
        result = agent_executor.invoke(
            input={"input": prompt_template.format_prompt(name_of_person=name, keywords=keywords)}
        )
    else:
        return {"error": "No name supplied"}
    
    linkedin_profile_url = result["output"]
    
    return linkedin_profile_url
    #return os.getenv("MY_LINKEDIN_PROFILE")


if __name__ == "__main__":
    profile_url = lookup("Tim Jones","Upwind")#lookup(os.getenv("MY_NAME_TO_SEARCH"))
    print(profile_url) 

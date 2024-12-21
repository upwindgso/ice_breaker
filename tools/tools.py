
from langchain_community.tools.tavily_search import TavilySearchResults



def get_profile_url_tavily(name : str):
    """Searches for Linkedin or Twitter Profile page"""
    
    search = TavilySearchResults(
        max_results=10,
        search_depth="basic",
        #include_domains=["linkedin.com/in/"],
        exclude_domains=["rocketreach.co"],
    )
    res = search.run(f"{name}")

    return res


from langchain_community.utilities import SearxSearchWrapper

def get_profile_url_searxng(name : str):
    """Searches for Linkedin or Twitter Profile page"""

    search = SearxSearchWrapper(
        searx_host="http://localhost:8080"
    )
    res = search.results(
        f"{name}",
        num_results=10,
        categories="linkedin profile"
        )
    
    return res

if __name__ == "__main__":
    res = get_profile_url_searxng("Eden Marco Udemy site:linkedin.com/in/")

    print(res)

    #from reranker import rerank_results

    #reres = rerank_results("Eden Marco Udemy",res)

    #print(reres) 


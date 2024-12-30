
import requests

def rerank_results(query, passages):
    """Reranks the results based on relevance to the name."""
    response = requests.post(
        "http://localhost:8000/rerank",
        json={"query": query, "passages": passages}
    )
    return response.json()["response"]


from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name : str):
    """Searches for Linkedin or Twitter Profile page"""
    
    search = TavilySearchResults(
        max_results=20,
        search_depth="basic",
        #include_domains=["linkedin.com/in/"],
        exclude_domains=["rocketreach.co"],
    )
    res = search.run(f"{name}")

    return res


from langchain_community.utilities import SearxSearchWrapper

def get_profile_url_searxng(name : str, location: str = "", keywords: str = ""):
    """Searches for Linkedin or Twitter Profile page"""

    search = SearxSearchWrapper(
        searx_host="http://localhost:8080"
    )
    res = search.results(
        f"{name}",
        num_results=10,
        categories="linkedin profile"
        )
    
    # Extract snippets for reranking
    content = [f"{item.get('title', '')} - {item.get('snippet', '')}" for item in res]

    query = str(
            {"name" : name,
             "location" : location,
             "keywords" : keywords
             }
    )
    
    # Get reranking scores
    scores = rerank_results(query, content)

    # Add scores back to original results
    for item, score in zip(res, scores):
        item['rerank_score'] = float(score)  # Convert tensor to float if needed

    # Optional: Sort results by rerank score
    res = sorted(res, key=lambda x: x['rerank_score'], reverse=True)
    
    return res

if __name__ == "__main__":
    res = get_profile_url_searxng("Eden Marco Udemy site:linkedin.com/in/")


    print(res) 


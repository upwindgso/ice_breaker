
from langchain_community.tools.tavily_search import TavilySearchResults


import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_path = r"C:\GitHub\bge-reranker-v2-m3"

from FlagEmbedding import FlagReranker

def rerank_results(query, passages):
    pairs = [[query, passage] for passage in passages]
    
    reranker = FlagReranker(model_path, normalize=True)

    score = reranker.compute_score(pairs)
    
    return score
""""
if __name__ == "__main__":
    query = "What is the capital of France?"
    passages = [
        "Paris is the capital of France.",
        "London is the capital of England.",
        "Berlin is the capital of Germany."
    ]
    scores = rerank_results(query, passages)
    print(scores)
"""

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
    
    # Extract snippets for reranking
    snippets = [item['snippet'] for item in res]

    # Get reranking scores
    scores = rerank_results(name, snippets)

    # Add scores back to original results
    for item, score in zip(res, scores):
        item['rerank_score'] = float(score)  # Convert tensor to float if needed

    # Optional: Sort results by rerank score
    res = sorted(res, key=lambda x: x['rerank_score'], reverse=True)
    
    return res

if __name__ == "__main__":
    res = get_profile_url_searxng("Eden Marco Udemy site:linkedin.com/in/")


    print(res) 


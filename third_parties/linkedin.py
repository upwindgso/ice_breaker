import os
from click.core import V
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    #the comment below informs langchain on whetehr to use the tool or not
    """Scrape information from LinkedIn profiles,
        Manually scrape the information from the LinkedIn profile
    """   

    if mock:
        linkedin_profile_url = os.getenv("LI_TEST_GIST")
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.getenv("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
        if response.status_code != 200:
            return {"error": "Unable to fetch LinkedIn profile"}
    
    data = response.json()
    
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "recommendations","similarly_named_profiles"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            try:
                group_dict.pop("profile_pic_url_large")
            except:
                pass

    
    return data



if __name__ == "__main__":
    
    liprofile = os.getenv("MY_LINKEDIN_PROFILE")

    print(
        scrape_linkedin_profile(
            linkedin_profile_url=liprofile,mock=True
        )

    )
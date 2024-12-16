from email import header
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
api_key = os.getenv('PROXYCURL_API_KEY')
header_dic = {'Authorization': f'Bearer {api_key}'}
params = {
    'url': os.getenv("MY_LINKEDIN_PROFILE"),
}

"""
response = requests.get(
    api_endpoint,
    headers=header_dic,
    params=params,
)
"""

response = requests.get(os.getenv("LI_TEST_GIST"))

data = response.json()
# Print the data returned by the API
print(data)
if response.status_code == 200:
    # Process the JSON data as needed
    pass
else:
    print(f'Failed to retrieve LinkedIn profile: {response.status_code}')

print(data['full_name'])





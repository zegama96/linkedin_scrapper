import os
import requests


def scrape_linkedin_profile(linkedin_profile_url=""):
    """
    scrape information from Linkedin Profile

    :param linkedin_profile_url:
    :return:
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dict = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        # api_endpoint, params={"url": linkedin_profile_url}, headers=header_dict
    )
    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

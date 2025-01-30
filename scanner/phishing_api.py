import requests
from utils.logger import log_message

def check_phishtank(url):
    API_URL = "https://phishtank.com/check_url/"
    response = requests.post(API_URL, data={'url': url})
    if "phishing" in response.text.lower():
        log_message("warning", f"{url} found in PhishTank database")
        return True
    return False

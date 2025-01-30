from bs4 import BeautifulSoup
import requests
from utils.logger import log_message

def scan_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        suspicious_words = ["login", "password", "verify account", "credit card"]
        for word in suspicious_words:
            if word in soup.text.lower():
                log_message("warning", f"Suspicious content detected on {url}")
                return True
        return False
    except Exception:
        log_message("error", f"Failed to scan content for {url}")
        return False
from Levenshtein import distance
from utils.logger import log_message

def check_similarity(url, popular_sites):
    for site in popular_sites:
        if distance(url, site) < 3:
            log_message("warning", f"{url} is similar to {site} (Possible phishing)")
            return True
    return False
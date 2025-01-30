import whois
import tldextract
from datetime import datetime
from utils.logger import log_message

def check_url(url):
    root_domain = None  # הגדרת המשתנה מראש

    try:
        # חילוץ הדומיין הראשי בלבד (למשל, herokuapp.com מתוך juice-shop.herokuapp.com)
        extracted = tldextract.extract(url)
        root_domain = f"{extracted.domain}.{extracted.suffix}"  # למשל: herokuapp.com

        # בדיקה האם הדומיין הוא root domain
        if extracted.subdomain:
            log_message("warning", f"Skipping WHOIS for subdomain: {url}")
            return 50, "⚠️ Suspicious (Subdomain, no WHOIS data)"

        # ביצוע WHOIS רק על הדומיין הראשי
        try:
            domain_info = whois.whois(root_domain)
        except Exception as e:
            if "No match for" in str(e):
                log_message("error", f"WHOIS data not found for {root_domain}")
                return 100, "❌ Unknown (No WHOIS Data)"
            raise e  # זריקת השגיאה מחדש אם זו בעיה אחרת

        # בדיקת גיל הדומיין
        creation_date = domain_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if not creation_date:
            log_message("error", f"WHOIS data found but no creation date for {root_domain}")
            return 100, "❌ Unknown (No Creation Date)"

        domain_age = (datetime.now() - creation_date).days
        log_message("info", f"Checked {root_domain} - Age: {domain_age} days")

        # קביעת רמת סכנה לפי גיל הדומיין
        if domain_age < 90:
            return 80, "❌ Dangerous (New Domain)"
        elif domain_age < 365:
            return 50, "⚠️ Suspicious (Relatively New)"
        else:
            return 20, "✅ Safe"

    except Exception as e:
        log_message("error", f"Error checking {root_domain if root_domain else url}: {str(e)}")
        return 100, "❌ Unknown (Error Checking Domain)"

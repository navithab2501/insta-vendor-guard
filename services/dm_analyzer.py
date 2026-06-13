import re

def analyze_dm(text):

    text = text.lower()

    risk_keywords = ["advance", "pay first", "urgent", "scam", "fraud"]
    safe_keywords = ["cod", "cash on delivery", "pay after"]

    contact_pattern = r"\b\d{10}\b"

    risk_found = [k for k in risk_keywords if k in text]
    safe_found = [k for k in safe_keywords if k in text]

    contact_found = re.findall(contact_pattern, text)

    return {
        "risk_count": len(risk_found),
        "safe_count": len(safe_found),
        "risk_keywords": risk_found,
        "safe_keywords": safe_found,
        "contact_number_found": len(contact_found)
    }
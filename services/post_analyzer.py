import re

def analyze_post(text):

    text = text.lower()

    scam_keywords = ["free", "earn money", "investment", "double money", "loan", "click link"]
    found = [k for k in scam_keywords if k in text]

    # 🔥 COMMENT SECTION RISK DETECTION
    comment_risk_keywords = ["dm me", "message me", "limited offer", "fast reply"]

    comment_risk_count = sum(1 for k in comment_risk_keywords if k in text)

    return {
        "keyword_count": len(found),
        "found_keywords": found,
        "comment_risk_count": comment_risk_count
    }
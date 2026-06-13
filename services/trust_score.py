def calculate_trust_score(bio_data, post_data, dm_data):

    score = 50
    reasons = []

    # ---------------- BIO ----------------
    followers = bio_data.get("followers_count", 0)
    following = bio_data.get("following_count", 0)
    bio_text = bio_data.get("bio_text", "").lower()

    if followers > following * 2:
        score += 20
        reasons.append("Strong follower base detected.")

    elif followers < following:
        score -= 20
        reasons.append("Following higher than followers (risk signal).")

    if "free" in bio_text or "earn money" in bio_text or "investment" in bio_text:
        score -= 15
        reasons.append("Suspicious words found in bio.")

    # ---------------- POST + COMMENTS ----------------
    keyword_count = post_data.get("keyword_count", 0)
    comment_risk = post_data.get("comment_risk_count", 0)

    if keyword_count > 0:
        penalty = keyword_count * 8
        score -= penalty
        reasons.append(f"Post scam keywords detected (-{penalty}).")

    if comment_risk > 0:
        penalty = comment_risk * 10
        score -= penalty
        reasons.append("Suspicious DM/comment bait detected.")

    # ---------------- DM ----------------
    risk_count = dm_data.get("risk_count", 0)
    safe_count = dm_data.get("safe_count", 0)
    contact_found = dm_data.get("contact_number_found", 0)

    if risk_count > 0:
        penalty = risk_count * 15
        score -= penalty
        reasons.append("Risky payment/scam keywords in DM.")

    if safe_count > 0:
        score += safe_count * 8
        reasons.append("Safe payment signals detected (COD etc.).")

    if contact_found > 0:
        score -= 25
        reasons.append("Contact number shared in DM (high scam risk).")

    # ---------------- LIMIT ----------------
    score = max(0, min(100, score))

    # ---------------- STATUS ----------------
    if score >= 75:
        status = "🟢 GENUINE"
        message = "Low risk account. Still verify before payment."

    elif score >= 45:
        status = "🟠 SUSPICIOUS"
        message = "Moderate risk detected. Be careful."

    else:
        status = "🔴 HIGH RISK / FAKE"
        message = "High scam probability. Avoid advance payment."

    return {
        "trust_score": score,
        "status": status,
        "message": message,
        "reasons": reasons
    }
from flask import Flask, render_template, request
import os

from services.ocr_service import extract_text
from services.bio_analyzer import analyze_bio
from services.post_analyzer import analyze_post
from services.dm_analyzer import analyze_dm
from services.trust_score import calculate_trust_score

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    bio_image = request.files.get("bio_image")
    post_image = request.files.get("post_image")
    dm_image = request.files.get("dm_image")

    # ---------------- DEFAULT STRUCTURE ----------------

    bio_data = {
        "followers_count": 0,
        "following_count": 0,
        "bio_text": ""
    }

    post_data = {
        "keyword_count": 0,
        "found_keywords": [],
        "comment_risk_count": 0
    }

    dm_data = {
        "risk_count": 0,
        "safe_count": 0,
        "risk_keywords": [],
        "safe_keywords": [],
        "contact_number_found": 0
    }

    # ---------------- BIO ----------------
    if bio_image and bio_image.filename:
        path = os.path.join(UPLOAD_FOLDER, bio_image.filename)
        bio_image.save(path)

        text = extract_text(path)
        bio_data = analyze_bio(text)
        bio_data["bio_text"] = text

    # ---------------- POST (POST + COMMENTS) ----------------
    if post_image and post_image.filename:
        path = os.path.join(UPLOAD_FOLDER, post_image.filename)
        post_image.save(path)

        text = extract_text(path)
        post_data = analyze_post(text)

    # ---------------- DM ----------------
    if dm_image and dm_image.filename:
        path = os.path.join(UPLOAD_FOLDER, dm_image.filename)
        dm_image.save(path)

        text = extract_text(path)
        dm_data = analyze_dm(text)

    # ---------------- DEBUG ----------------
    print("BIO:", bio_data)
    print("POST:", post_data)
    print("DM:", dm_data)

    # ---------------- TRUST SCORE ----------------
    result = calculate_trust_score(bio_data, post_data, dm_data)

    return render_template(
        "result.html",
        bio=bio_data,
        post=post_data,
        dm=dm_data,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
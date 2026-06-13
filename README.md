# Insta Vendor Guard

## 📌 Project Overview

Insta Vendor Guard is a web application that helps users identify potentially fraudulent Instagram vendors by analyzing uploaded screenshots using OCR (Optical Character Recognition) and rule-based risk analysis.

The application extracts text from Instagram screenshots and evaluates various trust factors to generate a Trust Score and provide recommendations.

---

## 🚀 Features

* 📷 Bio Screenshot Analysis
* 🛍️ Post Screenshot Analysis
* 💬 DM Screenshot Analysis
* 🔍 OCR-based Text Extraction using EasyOCR
* ⚠️ Scam Keyword Detection
* 💰 Advance Payment Detection
* 🚚 Cash on Delivery (COD) Check
* 📊 Trust Score Calculation (0–100)
* 🟢 Low Risk / 🟠 Be Careful / 🔴 High Risk Recommendation

---

## 🛠️ Technologies Used

* Python
* Flask
* EasyOCR
* HTML
* CSS

---

## 📂 Project Structure

```
insta_vendor_guard/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   ├── uploads/
│   └── images/
│
└── services/
    ├── ocr_service.py
    ├── bio_analyzer.py
    ├── post_analyzer.py
    ├── dm_analyzer.py
    └── trust_score.py
```

---

## ▶️ How to Run

1. Install the required packages:

```
pip install -r requirements.txt
```

2. Run the application:

```
py app.py
```

3. Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

* AI-based scam detection
* Fake profile prediction
* UPI ID and bank account verification
* Improved trust score algorithm
* Advanced Instagram profile analysis

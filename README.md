
# YouTube Video Success Prediction 🚀

This project predicts the success (view counts) of YouTube videos based on metadata like title, description, and publish time.

---


---

## 📈 Highlights

- **Feature Engineering**: Title length, word counts, question mark detection, numbers, description quality, publication time, engagement ratios.
- **ML Model**: Random Forest Regressor to predict log-transformed YouTube view counts.
- **API Serving**: FastAPI app providing real-time predictions based on video metadata.
- **Statistical Testing**: Analyzed real data to answer business questions using appropriate statistical methods.

---

## 📊 Product Insights and Statistical Testing

We explored **real-world YouTube metadata** to answer key business/product questions:

| Question | Method | Result |
|:---------|:-------|:-------|
| Are some days better for publishing podcasts? | Kruskal-Wallis Test | Tested for differences in view counts by publishing day. |
| Does longer description help views? | Spearman Correlation | Checked correlation between description length and views. |
| Does mentioning 'subscribe' boost views? | Mann-Whitney U Test | Analyzed impact of call-to-action words on views. |

Statistical methods were selected based on data properties (normality, skewness), demonstrating practical analytics skills used in real product and marketing teams.

---

## 🚀 How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Start FastAPI server:

```
uvicorn app:app --reload
```

3. Open browser at:

```
http://127.0.0.1:8000/docs
```

Use the API Swagger UI to test the prediction endpoint!

---

## 👨‍💻 Author

Built with ❤️ by Jwalith

---

# === End of README.md ===

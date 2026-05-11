# 🎓 AI-Based Smart Career Counseling Expert System
### GUI Version — Streamlit | KRR Project

---

## 📁 Project Files

```
career_counseling_gui/
├── app.py              ← Main Streamlit GUI (run this)
├── knowledge_base.py   ← Knowledge Base (all career rules)
├── inference_engine.py ← Forward Chaining Inference Engine
├── requirements.txt    ← Dependencies
└── README.md           ← This file
```

---

## ⚙️ Setup & Run (Step by Step)

### Step 1 — Install Python
Make sure Python 3.8+ is installed.
Download from: https://www.python.org/downloads/

### Step 2 — Install Streamlit
Open Command Prompt / Terminal and run:
```
pip install streamlit
```

### Step 3 — Run the App
Navigate to project folder:
```
cd career_counseling_gui
streamlit run app.py
```

The app will open automatically in your browser at:
**http://localhost:8501**

---

## ✅ Features

| Feature                  | Status |
|--------------------------|--------|
| Career Recommendation    | ✅     |
| Match Percentage         | ✅     |
| Explainable AI           | ✅     |
| Skill Gap Analysis       | ✅     |
| Career Roadmap           | ✅     |
| Personality Analysis     | ✅     |
| Weakness Analysis        | ✅     |
| Domain Filtering         | ✅     |
| Salary (PKR + USD)       | ✅     |
| Certifications Guide     | ✅     |
| Job Roles List           | ✅     |
| Dark Theme GUI           | ✅     |

---

## 🧠 KRR Concepts Used

| Concept                  | Implementation              |
|--------------------------|-----------------------------|
| Knowledge Base           | `knowledge_base.py`         |
| Inference Engine         | `inference_engine.py`       |
| Forward Chaining         | `run_inference_engine()`    |
| Rule-Based Reasoning     | IF-THEN weighted rules      |
| Expert System            | Full career counselor logic |

---

## 📊 Careers Covered (10 Total)

1. 🤖 AI Engineer
2. 📊 Data Scientist
3. 💻 Software Engineer
4. 🔐 Cybersecurity Expert
5. 🎨 Graphic Designer
6. 📈 Business Analyst
7. 🗂️ Project Manager
8. 🌐 Network Engineer
9. 🦾 Robotics Engineer
10. 🎮 Game Developer

---

## 💡 Viva Tips

**Q: What is Forward Chaining?**
A: Starts from known facts → applies rules → reaches conclusions.
   Facts (skills) → Rules (knowledge base) → Conclusion (career)

**Q: Why is this KRR?**
A: System stores expert knowledge as rules and applies logical
   reasoning through an inference engine to recommend careers.

**Q: How is scoring calculated?**
A: Each rule has a weight:
   - Required Skill matched: +15 points
   - Interest matched: +12 points
   - CGPA meets minimum: +10 points
   - Personality bonus: +5 points
   - Match % = (score / max_score) × 100

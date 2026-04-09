# 🚀 Flowlytics – Personal Productivity Analytics Engine

## 📌 Overview

**Flowlytics** is a data-driven productivity analysis system that evaluates daily performance based on study habits, task completion, sleep patterns, and screen time.

It transforms raw lifestyle data into **quantitative productivity scores** and **actionable insights**, helping users understand and improve their daily efficiency.

---

## 🧠 Problem Statement

Most students track tasks but **don’t measure productivity scientifically**.
Flowlytics bridges this gap by combining multiple behavioral factors into a single **Productivity Score**.

---

## ⚙️ Core Logic

### 📊 Metrics Computed

* **Completion Rate** = Tasks Completed / Tasks Planned
* **Sleep Score** (based on optimal sleep range)
* **Productivity Score** using weighted formula:

```id="c2k8l3"
Productivity Score =
(Study Hours × 0.4) +
(Completion Rate × 40) +
(Sleep Score × 0.2)
```

---

## 🔍 Insight Generation

The system generates personalized insights based on user behavior:

* Low productivity detection
* Sleep deficiency warnings
* Over-planning vs under-execution detection
* Screen time impact analysis
* Positive reinforcement for high productivity

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas
* **Data Source:** CSV dataset

---

## 📂 Project Structure

```id="w3d9xa"
Flowlytics/
│── main.py              # Core analysis script
│── flowlytics_data.csv  # Input dataset
│── README.md
```

---

## ▶️ How It Works

1. Load dataset using Pandas
2. Calculate completion rate
3. Assign sleep score based on sleep hours
4. Compute overall productivity score
5. Generate personalized insights
6. Display daily analysis

---

## ⚙️ Installation & Execution

```bash id="4c1l7y"
git clone https://github.com/your-username/flowlytics.git
cd flowlytics
pip install pandas
python main.py
```

---

## 📌 Sample Output

```id="q8z1mx"
Date: 2026-04-01
Productivity Score: 72.5

Insights:
- You are planning too much but completing less.
----------------------------------------
```

---

## 🚀 Future Improvements

* 📊 Interactive dashboard (Streamlit / Power BI)
* 🤖 ML-based productivity prediction
* 📱 Mobile-friendly interface
* 🔐 User-specific tracking system

---

## 💡 Key Learning Outcomes

* Data preprocessing using Pandas
* Feature engineering (custom scoring system)
* Rule-based insight generation
* Translating raw data into meaningful decisions

---

## 👤 Author

**Vaishnavi**

* GitHub:https://github.com/vaishnavisbhat22

---
<img width="1920" height="1080" alt="Screenshot 2026-03-26 194403" src="https://github.com/user-attachments/assets/021aa9b7-f003-4f56-bb9c-c0842c4c3905" />



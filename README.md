# 🚀 SaaS AI Growth Engine

## Overview
The **SaaS AI Growth Engine** is an end-to-end data pipeline and AI intervention system designed to process user telemetry data, identify churn-risk accounts, and automatically generate personalized re-engagement campaigns. 

This project bridges the gap between raw data engineering and actionable business intelligence, demonstrating how modern data stacks can directly drive revenue retention.

## 🛠️ Tech Stack
* **Database:** DuckDB
* **Data Transformation:** dbt (data build tool)
* **Analytics & Processing:** Python, Pandas
* **AI Integration:** Google Gemini AI API (`google-genai`)
* **Visualization:** Streamlit

## 📊 Core Features
1. **Automated Data Pipeline:** Ingests raw user telemetry data (logins, feature usage) and transforms it into clean, structured models using **dbt** and **DuckDB**.
2. **Cohort & Churn Analysis:** Segments users into actionable categories (e.g., Active, High Value, Churn Risk) based on usage thresholds using **Python** and **Pandas**.
3. **AI-Driven Intervention:** Queries the database for at-risk users and leverages the **Google Gemini API** to automatically generate personalized, context-aware re-engagement emails.
4. **Interactive Dashboard:** Visualizes real-time metrics, user segmentation breakdowns, and raw data outputs through a clean **Streamlit** web app.

## 🏗️ Project Architecture
* `data/raw/`: Contains raw CSV telemetry exports.
* `telemetry_analytics/`: The dbt project handling data transformations and building the `user_summary` view.
* `scripts/`: Python scripts for database querying, API integration (`ai_intervention.py`), and the Streamlit dashboard (`dashboard.py`).
* `notebooks/`: Jupyter notebooks used for initial cohort analysis and exploratory data analysis.

## 🚀 How to Run Locally

**1. Clone the repository and install dependencies:**
```bash
git clone [https://github.com/YourUsername/saas-ai-growth-engine.git](https://github.com/YourUsername/saas-ai-growth-engine.git)
cd saas-ai-growth-engine
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
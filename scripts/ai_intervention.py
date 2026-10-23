import duckdb
import pandas as pd
from google import genai
import os
from dotenv import load_dotenv

# 1. Load the API key securely
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key not found. Please check your .env file.")

client = genai.Client(api_key=api_key)

# 2. Shift working directory so DuckDB finds the CSV files correctly
if os.path.exists('telemetry_analytics'):
    os.chdir('telemetry_analytics')
con = duckdb.connect(database='dev.duckdb', read_only=True)

# 3. Pull a sample of 3 Churn Risk users
query = """
SELECT name, company, total_events, last_active_date 
FROM main.user_summary 
WHERE user_segment = 'Churn Risk' 
LIMIT 3
"""
churn_users = con.execute(query).df()
print(f"Found {len(churn_users)} users at risk. Generating intervention emails...\n")

# 4. Generate emails using the updated 3.8 model
for index, user in churn_users.iterrows():
    prompt = f"""
    You are the Customer Success Manager at a SaaS company. 
    Write a short, friendly, 3-sentence re-engagement email to {user['name']} who works at {user['company']}. 
    They haven't logged in since {user['last_active_date']} and have only completed {user['total_events']} actions in our app. 
    Offer them a quick 10-minute check-in call to help them get more value out of the platform.
    Do not use generic placeholders like [Your Name]. Sign off as "The Data Team".
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        print(f"--- Automated Email for {user['name']} ---")
        print(response.text.strip())
        print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"\nERROR: Could not generate email for {user['name']}. Reason: {e}")
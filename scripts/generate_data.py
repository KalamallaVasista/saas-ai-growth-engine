import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
np.random.seed(42)

# Generate 1,000 Users
num_users = 1000
users = [{'user_id': i, 'name': fake.name(), 'company': fake.company(), 
          'signup_date': fake.date_between(start_date='-90d', end_date='today')} 
         for i in range(1, num_users + 1)]

users_df = pd.DataFrame(users)
users_df.to_csv('data/raw/users.csv', index=False)

# Generate Telemetry Events (Logins, Feature Clicks, etc.)
events = ['login', 'view_dashboard', 'use_core_feature', 'invite_team_member', 'upgrade_click']
log_data = []

for _, user in users_df.iterrows():
    is_active = random.choice([True, False])
    num_events = random.randint(20, 100) if is_active else random.randint(1, 15)
    
    current_date = user['signup_date']
    for _ in range(num_events):
        event = random.choices(events, weights=[0.4, 0.3, 0.2, 0.05, 0.05])[0]
        log_data.append({
            'event_id': fake.uuid4(),
            'user_id': user['user_id'],
            'event_type': event,
            'event_date': current_date
        })
        current_date += timedelta(days=random.randint(0, 3))
        if current_date > datetime.now().date():
            break

events_df = pd.DataFrame(log_data)
events_df.to_csv('data/raw/event_logs.csv', index=False)

print("Data generation complete! Files saved in data/raw/")
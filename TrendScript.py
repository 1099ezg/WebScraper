import json
from datetime import datetime, timedelta
import pytz
from collections import Counter

def load_trends(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [json.loads(line) for line in lines]

def extract_trends(trends_data, period_hours):
    central = pytz.timezone('US/Central')
    now = datetime.now(central)
    period_start = now - timedelta(hours=period_hours)

    hashtags = []
    for entry in trends_data:
        timestamp = datetime.fromisoformat(entry['timestamp']).astimezone(central)
        if timestamp > period_start:
            hashtags.extend([trend['name'] for trend in entry['trends']])

    return Counter(hashtags)

trends_data = load_trends('trends.json')

# Analyze trends for the last 1 hour and 8 hour
trending_1_hour = extract_trends(trends_data, 1)
trending_8_hour = extract_trends(trends_data, 8)


# Print the most common hashtags(Top 5)
print("Trending Hashtags in the past 1 Hour:")
for trend, count in trending_1_hour.most_common(5):
    print(f'{trend}: {count}')

print("Trending Hashtags in the last 8 Hours:")
for trend, count in trending_8_hour.most_common(5):
    print(f'{trend}: {count}')


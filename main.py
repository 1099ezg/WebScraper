import tweepy
import json
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv('TWITTER_API_KEY')
api_secret_key = os.getenv('TWITTER_API_SECRET_KEY')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Auth section
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)
woeid = 1

# Fetch current trending topics
trending_topics = api.get_place_trends(woeid)

# Time Zone Marker
central = pytz.timezone('US/Central')
current_time = datetime.now(central)

# Timestamp marker
data = {
    'timestamp': current_time.isoformat(),
    'trends': trending_topics[0]['trends']
}

with open('trends.json', 'a') as f:
    f.write(json.dumps(data) + "\n")

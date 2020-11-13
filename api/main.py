from flask import Flask,jsonify
from flask_cors import CORS
import simpleaudio as sa
import tweepy
from dotenv import load_dotenv
import os


load_dotenv()

CONSUMER_KEY=os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET=os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
tweet_data={}
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/<user>')
def get_tweets(user):
    tweets = api.user_timeline(screen_name=user)

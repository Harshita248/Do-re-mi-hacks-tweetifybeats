from flask import Flask,jsonify
from flask_cors import CORS
import simpleaudio as sa
import tweepy
from dotenv import load_dotenv
import os
import re
import time

load_dotenv()

CONSUMER_KEY=os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET=os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
tweet_data=[]
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

path = "./audio/"

pianoNotes = {
    "1": path + "C.wav",
    "2": path + "D.wav",
    "3": path + "E.wav",
    "4": path + "F.wav",
    "5": path + "G.wav",
    "6": path + "A.wav",
    "7": path + "B.wav",
    "8": path + "C1.wav"
}

guitarNotes = {
    "1": path + "C_Guitar.wav",
    "2": path + "D_Guitar.wav",
    "3": path + "E_Guitar.wav",
    "4": path + "F_Guitar.wav",
    "5": path + "G_Guitar.wav",
    "6": path + "A_Guitar.wav",
    "7": path + "B_Guitar.wav",
}

xylophoneNotes = {
    "1": path + "C_Drum.wav",
    "2": path + "D_Drum.wav",
    "3": path + "E_Drum.wav",
    "4": path + "F_Drum.wav",
    "5": path + "G_Drum.wav",
    "6": path + "A_Drum.wav",
    "7": path + "B_Drum.wav",
    "8": path + "C1_Drum.wav"
}


def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


@app.route('/<user>')
def get_tweets(user):
    try:
        global tweet_data
        tweet_data=[]
        tweets = api.user_timeline(screen_name=user)
        for tweet in tweets[:3]:
            tweet_data.append(tweet.text)
        
        return jsonify({'user':user,'1':tweet_data[0],'2':tweet_data[1],'3':tweet_data[2]})
    except tweepy.error.TweepError:
        return jsonify({'status':'User not found'})

@app.route('/<user>/<int:num>')
def tweet_to_ascii(user,num):
    if num>3:
        return jsonify({'status':'Tweet not found'})
    else:
        global tweet_data
        ascii_conv=[]
        for elem in deEmojify(tweet_data[num-1]).split():
            ascii_conv.extend((int(ord(n)/18)) for n in elem)
        return jsonify({'ASCII':ascii_conv}) 

@app.route('/<user>/<int:num>/<string:instrument>')
def tweet_to_music(user,num,instrument):
    if num>3:
        return jsonify({'status':'Tweet not found'})
    else:
        global tweet_data
        ascii_conv=[]
        for elem in deEmojify(tweet_data[num-1]).split():
            ascii_conv.extend((int(ord(n)/18)) for n in elem)
        if instrument.lower()=='piano':
            for i in ascii_conv:
                wave_obj = sa.WaveObject.from_wave_file(pianoNotes.get(str(i)))
                time.sleep(.5)
                play_obj = wave_obj.play() 
        if instrument.lower()=='guitar':
            for i in ascii_conv:
                wave_obj = sa.WaveObject.from_wave_file(guitarNotes.get(str(i)))
                time.sleep(.5)
                play_obj = wave_obj.play() 
        if instrument.lower()=='xylophone':
            for i in ascii_conv:
                wave_obj = sa.WaveObject.from_wave_file(xylophoneNotes.get(str(i)))
                time.sleep(.5)
                play_obj = wave_obj.play() 
        return "playing"
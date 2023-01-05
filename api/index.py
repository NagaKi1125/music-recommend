
from recommendation import MusicRecommendation
from flask import Flask, redirect, url_for, request
import joblib
app = Flask(__name__)

music_recommend = MusicRecommendation()
file_name = 'model.joblib'
song_cluster_pipeline = joblib.load(file_name)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
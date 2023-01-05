

from flask import Flask, request
import joblib

from recommendation import MusicRecommendation

app = Flask(__name__)

music_recommend = MusicRecommendation()
file_name = '../model.joblib'
song_cluster_pipeline = joblib.load(file_name)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/recommend', methods=['GET'])
def recommendation():
    seedList = request.get_json()
    result = music_recommend.main(seedList=seedList, song_cluster_pipeline=song_cluster_pipeline)

    return result


@app.route('/auto-gen/fetch-track', methods=['GET'])
def fetch_track():
    result = music_recommend.fetchTrack()
    return result


# data analyze
@app.route('/auto-gen/artists', methods=['GET'])
def get_artists():
    artists = music_recommend.getArtists()
    return artists


@app.route('/auto-gen/getTrack', methods=['GET'])
def get_tracks():
    seedList = request.get_json()
    music_list = []
    for r in seedList:
        track = music_recommend.getTrackInformation(trackId=r['id'], year=r['year'])
        music_list.append(track)
    return music_list

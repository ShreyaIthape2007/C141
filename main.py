from flask import Flask,jsonify,request

import csv

all_movies = list()

with open('movies.csv') as f:
    csv_reader=csv.reader(f)
    data = list(csv_reader)
    all_movies = data[1:]

did_not_watch_movies = list()

liked_movies = list()

not_liked_movies = list()

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    }),200
@app.route("/liked-movie",methods=["POST"])
def liked_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),200
@app.route("/not-liked-movies",methods=["POST"])
def not_liked_movie():
    global all_movies
    movie = all_movies[0]
    all_movies - all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),200
@app.route("/did-not-watch-movies",methods=["POST"])
def did_not_watch_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch_movies.append(movie)
    return jsonify({
        "status":'success'
    }),200

if __name__ == "__main__":
    app.run()

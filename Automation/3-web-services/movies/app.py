from flask import Flask, render_template, redirect, url_for
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    onlyfiles = [f for f in listdir("static") if isfile(join("static", f))]
    movies = []
    for f in onlyfiles:
        movies.append(f.strip(".html"))
    return render_template("index.html", len=len(movies), movies=sorted(movies))

@app.route("/<movie_id>")
def movie(movie_id):
    return redirect(url_for('static', filename=movie_id+'.html'))


if __name__ == "__main__":
    app.run()
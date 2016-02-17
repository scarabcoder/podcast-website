from app import app
from flask import render_template
from flask import abort
import feedparser
import re
feed = feedparser.parse('http://kidswhocode.podomatic.com/rss2.xml').entries
updated = []
x = 0

for item in feed:

    updated.append(item.title.replace(" ", "-").replace("?", "").lower())
    x = x + 1



for item in updated:
    print item
@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html',
                            feed=feed,
                            title = 'Scarab\'s blog')

@app.route("/episode/<episode>")
def show_episode(episode):
    print episode.lower()
    if(episode.lower() in updated):
        item = feed[updated.index(episode.lower())]
        return render_template("episode.html", item=item, img = item.image.href)
    else:
        abort(404)
@app.route("/episode/latest")
def show_latest():
    return render_template("episode.html", item=feed[0])
@app.route("/about")
def show_about():
    return render_template("about.html")
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

from flask import Flask
from flask import render_template
import feedparser
from flask import request
app = Flask(__name__)

RSS_FEED_DICT = {
    "ryf": "https://www.ruanyifeng.com/blog/atom.xml",
    "fox": "https://feeds.foxnews.com/foxnews/latest",
    "iol": "https://www.iol.co.za/cmlink/1.640",
}


# @app.route("/")
# @app.route("/ryf")
# def ryf():
#     return get_news("ryf")
#
#
# @app.route("/fox")
# def fox():
#     return get_news("fox")

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEED_DICT:
        publication = "ryf"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEED_DICT.get(publication))
    first_article = feed["entries"][0]
    return render_template("home.html", articles=feed["entries"])


if __name__ == "__main__":
    app.run(port=5000, debug=True)

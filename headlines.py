from flask import Flask
import feedparser

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
@app.route("/<published>")
def get_news(published='ryf'):
    feed = feedparser.parse(RSS_FEED_DICT.get(published))
    first_article = feed["entries"][0]
    return """<html>
        <body>
            <h1> {3} </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
            </body>
        </html>""".format(first_article.get("title"),
                          first_article.get("published"),
                          first_article.get("summary"),
                          feed["feed"].get("title"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)

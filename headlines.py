from flask import Flask
import feedparser

app = Flask(__name__)

RSS_FEED = "https://www.ruanyifeng.com/blog/atom.xml"

@app.route("/")
def get_news():
    feed = feedparser.parse(RSS_FEED)
    # print(feed)
    first_article = feed["entries"][0]
    return """<html>
        <body>
            <h1> 阮一峰的网络日志 </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
            </body>
        </html>""".format(first_article.get("title"),
                          first_article.get("published"),
                          first_article.get("summary"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)

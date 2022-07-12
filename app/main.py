from flask import Flask, render_template, request
from .tools.web_scraping import get_urls
from .tools.web_scraping import web_scrape
from .tools.web_scraping import validation_lists
from .tools.utils import utils

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', )

@app.route("/result", methods=["POST", "GET"])
def result():
  if request.method == "GET":
    # 1. Get the urls from the urls scraper

    movie_name = f"${request.url.split('movie_name=')[1].strip()} titles"
    urls = get_urls.method2(movie_name)

    # 2. Using the urls to scrape data, and get the data back.
    data = utils.removeEmptyList(web_scrape.scrapeUrls(urls))
    print(data)

    # 3. Send data back and render it.
    return render_template('queries.html', data=data)

  return render_template('index.html')

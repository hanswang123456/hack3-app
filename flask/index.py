from flask import Flask, render_template, request
import tools.web_scraping.get_urls as getURL
import tools.web_scraping.web_scrape as webScraper
import tools.utils.utils as util

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result", methods=["POST", "GET"])
def result():
  if request.method == "GET":
    # 1. Get the urls from the urls scraper
    specific_site = "cbr.com"
    movie_name = f"site:${specific_site} ${request.url.split('movie_name=')[1].strip()}"
    urls = getURL.method2(movie_name)
    print(urls)

    # 2. Using the urls to scrape data, and get the data back.
    data = util.removeEmptyList(webScraper.scrapeUrls(urls))
    print(data)

    # 3. Send data back and render it.
    return render_template('queries.html', data="0")

  return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)

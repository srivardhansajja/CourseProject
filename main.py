from flask import Flask, request, render_template
from crawler.crawler_handler import webcrawl
from model_deploy.model_dep import model_deploy


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html', result=False)


@app.route('/model', methods=['POST'])
def model():

    primary_url = request.form['primary_url']
    unfiltered_urls, stats = webcrawl(primary_url)
    filtered_urls = model_deploy(unfiltered_urls)

    stats['urls_found'] = len(filtered_urls)
    stats['url'] = primary_url

    return render_template('index.html', result=True, 
                                         faculty_page_urls=filtered_urls,
                                         stats = stats)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=3002)

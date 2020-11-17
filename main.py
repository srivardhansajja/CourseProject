from flask import Flask, request, render_template
from crawler_handler import webcrawl

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html', result=False)


@app.route('/model', methods=['POST'])
def model():

    primary_url = request.form['primary_url']
    webcrawl(primary_url)

    urls = []
    with open('matched_urls.jsonl', 'r') as f:
        for line in f:
            urls.append(line)

    return render_template('index.html', result=True, faculty_page_urls=urls)


if __name__ == "__main__":
    app.run(debug=True, port=2996)

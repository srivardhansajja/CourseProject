from flask import Flask, request, render_template
from crawler import webcrawl

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', result=False)

@app.route('/model', methods=['POST'])
def model():
    primary_url = request.form['primary_url']
    urls = webcrawl(primary_url)
    return render_template('index.html', result=True, faculty_page_urls=urls)

if __name__ == "__main__":
    app.run(debug=True)

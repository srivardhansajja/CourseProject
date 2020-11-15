from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', result=False)

@app.route('/model', methods=['POST'])
def model():
    return render_template('index.html', result=True, value='Hello')

if __name__ == "__main__":
    app.run(debug=True)

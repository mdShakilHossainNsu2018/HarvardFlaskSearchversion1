from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)


WORDS = []
with open('large', 'r') as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/search')
def search():
    qs = request.args.get('q')
    words = []
    for word in WORDS:
        if word.startswith(qs):
            words.append(word)
    # words = [word for word in WORDS if word.startswith(request.args.get('q'))]
    return render_template('results.html', words=words)


if __name__ == '__main__':
    app.run()

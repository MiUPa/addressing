from flask import Flask, render_template, jsonify
app = Flask(__name__)

quotes = [
    {"text": "I don't touch the gays... I'm saving that for marriage!", "character": "Angel Dust"},
    {"text": "Inside of every demon is a rainbow", "character": "Charlie"},
    {"text": "I can suck your dick!", "character": "Angel Dust"},
    {"text": "Ha! No.", "character": "Alastor"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-quote')
def get_quote():
    import random
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

with open('pokeneas.json', 'r') as file:
    pokeneas = json.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pokenea', methods=['GET'])
def pokeneaJSON():
    pokenea = random.choice(pokeneas)
    organizado = json.dumps(pokenea, sort_keys=False, indent=4)
    return '<pre>' + organizado + '</pre>'

@app.route('/pokeneAleatorio')
def pokeneAleatorio():
    pokenea = random.choice(pokeneas)
    return render_template('pokeneAleatorio.html', pokenea = pokenea)

if __name__ == "__main__":
    app.run(debug=True)
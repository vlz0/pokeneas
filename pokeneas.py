from flask import Flask, render_template, jsonify
import json
import random
import os

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
    contenedor = os.uname()[1] 
    return render_template('pokeneAleatorio.html', pokenea = pokenea, contenedor = contenedor)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
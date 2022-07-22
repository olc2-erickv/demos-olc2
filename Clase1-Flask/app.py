from flask import Flask, request, render_template
from analizador.parser import parser

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/api/interpretar', methods=['POST'])
def interpretar():
    if request.method == 'POST':
        result = parser.parse('2 * 3 + 4 * (5 - 4)')
        return {
            'resultado': result
        }

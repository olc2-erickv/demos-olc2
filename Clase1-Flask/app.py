from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/api/interpretar', methods=['POST'])
def interpretar(): 
    if request.method == 'POST':
        print('Metodo Post')

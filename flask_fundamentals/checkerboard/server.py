from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', times1 = 8, times = 8, color = 'black', color1 = 'red')

@app.route('/<num>')
def repeat(num):
    return render_template('index.html', times1 = int(num), times = 8, color = 'black', color1 = 'red')

@app.route('/<num>/<num1>')
def repeatBoth(num, num1):
    return render_template('index.html', times1 = int(num), times = int(num1), color = 'black', color1 = 'red')

@app.route('/<num>/<num1>/<color>/<color1>')
def colorChange(num, num1, color, color1):
    return render_template('index.html', times1 = int(num), times = int(num1), color = color, color1 = color1)

if __name__ == '__main__':
    app.run(debug=True)
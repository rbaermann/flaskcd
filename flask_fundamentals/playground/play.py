from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html', times=3, color = 'yellow')

@app.route('/play/<num>')
def repeat(num):
    return render_template('index.html', times = int(num), color = 'yellow')

@app.route('/play/<num>/<color>')
def color(num, color):
    return render_template('index.html', times = int(num), color = color)



if __name__ == '__main__':
    app.run(debug=True)
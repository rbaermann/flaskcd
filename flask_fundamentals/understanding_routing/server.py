from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def sayName(name):
    print(name)
    return 'Hi ' + name + '!'

@app.route("/repeat/<num>/<rand>")
def repeat(num, rand=''):
    print(rand)
    return rand * int(num)




if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return '<html><body><h1>Hello Bimal</h1></body></html>'


@app.route('/neel')
def index2():
   return '<html><body><h1>Hello Neel</h1></body></html>'

@app.route('/input/<name>')
def index3(name):
    fruits = ["apple", "banana", "cherry"]
    fruits.append('Dragon fruit')
    matched = False
    for fruit in fruits:
        if name == fruit:
            matched = True
    Output = ""
    if matched:
        Output = "Hell yeah"
    else:
        Output = "Hell yeah We didn't get a match"
    
    return Output

if __name__ == '__main__':
   app.run()
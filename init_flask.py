from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return '<html><body><h1>Hello Bimal</h1></body></html>'


@app.route('/neel')
def index2():
   return '<html><body><h1>Hello Neel</h1></body></html>'

if __name__ == '__main__':
   app.run()
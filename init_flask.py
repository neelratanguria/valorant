from flask import Flask, render_template, request
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

@app.route('/fridge', methods=['GET', 'POST'])
def appFridge():
    if request.method == 'GET':
        return render_template('fridge_app.html')
    if request.method == 'POST':
        # Get value from user submission (ie from html html template using key faal)
        faal = request.form['faal']
        # Lets define our list again
        fruits = ["apple", "banana", "cherry"]
        # boolean to check if we matched the fruit
        matched = False
        # Iterate through fruits list and check if faal matches any fruit in list
        for fruit in fruits:
            if faal == fruit:
                # Change boolean to true when the faal matches any fruit in list
                matched = True
        # Initialize Output variable
        Output = ""
        if matched:
            Output = "Hell yeah"
        else:
            Output = "Hell yeah We didn't get a match"
        return render_template('results.html',  Output=Output)

if __name__ == '__main__':
   app.run()
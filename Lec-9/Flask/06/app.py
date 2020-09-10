from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:name>')
def index(name):
    return render_template("index.html",user=name)

if __name__ == "__main__":
    app.run(debug=True)

'''
Let's understand
5 - We are taking data and storing in variable called "name"
6 - defining function associated with that URL and passing name variable
7 - using render_template serving html page containing name varible which get replaced by user variable
'''
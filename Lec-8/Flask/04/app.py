from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

'''
render_template function from flask allow us to serve html template through which we can make webpage more attractive and dynamic.
By default it search template in templates directory in the base path. Base path is a path where your main application app.py is saved.
'''
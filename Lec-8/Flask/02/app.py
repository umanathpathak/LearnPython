from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello !!!")

#In below function we are taking STRING data from URL and passing to function.
@app.route('/<string:name>')
def name(name):
    return("Hello {}".format(name))

#In below function we are taking INTEGER data from URL and passing to function.
@app.route('/<int:age>')
def age(age):
    return("Your age is {}".format(age))

@app.route('/<string:user>/<int:age>')
def usernage(user,age):
    return("Hello {}, your age is {}".format(user,age))


if __name__ == "__main__":
    app.run(debug=True)
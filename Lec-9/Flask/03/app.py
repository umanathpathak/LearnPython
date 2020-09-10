from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello !!!")

@app.route('/<string:name>')
def name(name):
    return("Hello {}".format(name))

@app.route('/<int:age>')
def age(age):
    return("Your age is {}".format(age))

# To work with data, there are two type of HTTP methods available
#GET - GET is used to request data from a specified resource.
#POST - POST is used to send data to a server to create/update a resource.

#@app.route('/<string:user>/<int:age>',methods=['get','post'])
#@app.route('/<string:user>/<int:age>',methods=['post'])
@app.route('/<string:user>/<int:age>',methods=['get'])
def usernage(user,age):
    return("Hello {}, your age is {}".format(user,age))


if __name__ == "__main__":
    app.run(debug=True)
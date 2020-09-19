from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello !!!")

if __name__ == "__main__":
    app.run()

'''
Lets understand this.
line no 1 - we are importing Flask class from flask module
line no 3 - Flask class taking current file as a argument. 
            This is main line which actually create flask application. 
            Just assume blank flask application and we are going to fillup data as per our requirement.
line no 5 - Using route decorator we tells the application which function get called for that particular URL.
line no 6-7 - defining function for the route URL
line no 9-10 - after confirming that this is main application file, we are starting flask application.
'''
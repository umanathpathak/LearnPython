from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST' and 'msg' in request.form:
        data = request.form.get('msg')
        return render_template("index.html",data=data)
    else:
        data=''
        return render_template("index.html")
    data=''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

'''
Let's understand
5 - We are allowing both method as very first time, it will use GET method and when we type some data and click on button that time it will use POST method
7-9 - defining function associated with that URL and checking http method, if it is POST then serv html page with given data
10-14 - If http method is not post then serv page with blank data
'''
from flask import Flask, render_template
from datetime import datetime


app = Flask("Timer Workout")



@app.route("/")
def Landing():
    return render_template("Landing_Page.html")
    
def footer():
    footerdb = open("footer.txt")
    for i in range (3):
        footerdb.write("footer.txt" + " by Carlos Teixeira")
    footerdb.close()
    return footer


# basically i have to defined a route its not defined????

@app.route("/index.html/")
def Home():
    return render_template("index.html")

def date():
    return ('Current Date and Time: {}'.format(datetime.datetime.now()))



if "Timer Workout" == "__main__":
    app.run()
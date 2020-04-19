import flask
import Timer
app = flask.Flask("Timer Workout")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

@app.route("/")
def Homepage():
    return get_html("Landing_Page")
    return ("timer")

@app.route("/")
def Landing():
    return get_html("index")


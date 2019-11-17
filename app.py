from flask import Flask, render_template, request
# from waitress import serve
import uuid, sys, os, re
from test import sum

app = Flask(__name__)


@app.after_request
def add_hostname_header(response):
    env_host = str(os.environ.get('HOSTNAME'))
    hostname = re.findall('[a-z]{3}-\d$', env_host)
    if hostname:
            response.headers["SP-LOCATION"] = hostname
    return response

@app.route('/')
def homepage():
    try:
        return render_template("index.html")
    except Exception as e:
	    return render_template("500.html", error = str(e))

@app.route('/uuid', methods=['POST'])
def get_uuid():
    try:
        uuid_p = str(uuid.uuid4())
        return render_template("index.html", uuid=uuid_p)
    except Exception as e:
	    return render_template("500.html", error = str(e))

@app.route('/sum', methods=['POST'])
def sumh():
    try:
        a = request.form.get("a")
        b = request.form.get("b")
        # a = 4
        # b = 1
        # sumn = a + b
        sumn = test.sum(a,b)
        return render_template("main.html", sumn=sumn)
    except Exception as e:
	    return render_template("500.html", error = str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    serve(app, listen='*:8081')

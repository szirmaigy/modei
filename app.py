from flask import Flask, render_template, request
# from waitress import serve
import uuid, sys, os, re
from test import sum
from domaininfo import DInfo

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
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        sumn = sum(a,b)
        return render_template("index.html", sumn=sumn)
    except Exception as e:
	    return render_template("500.html", error = str(e))

@app.route('/Domain', methods=['POST'])
def DomainI():
    try:
        DomainName = request.form.get('DomainName')
        Registrar = DInfo(DomainName)
        return render_template("index.html", Registrar=Registrar)
    except Exception as e:
	    return render_template("500.html", error = str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')

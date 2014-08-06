import os
from flask import Flask, request, render_template, send_from_directory, flash, redirect, url_for
from test import draw

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY') or 't0p s3cr3t'

@app.route("/", methods=('GET', 'POST'))
def hello():
    poem = request.form.get('poem',None)
    print poem
    draw('static/images/img.jpg','static/fonts/TAMu_Kadampari.ttf',(44, 53, 57), poem)
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

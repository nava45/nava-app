import os
import random
import time
from flask import Flask, request, render_template, send_from_directory, flash, redirect, url_for
from test import draw

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY') or 't0p s3cr3t'

def choose_border():
    
    return "static/images/6.png"

def choose_font():
    return "static/fonts/TAMu_Kadampari.ttf"

def choose_color():
    return (44, 53, 57)

@app.route("/", methods=('GET', 'POST'))
def hello(op=None):
    poem = request.form.get('poem',None)
    print "poem is",poem
    if poem:
        poem = poem.encode('utf-8')
        border_img = choose_border()
        font = choose_font()
        color = choose_color()
        draw(border_img,font,color, poem)
        #return render_template('index.html', op='images/output.png')
        #time.sleep(3)
        #return redirect(url_for('.hello', op="static/images/output.png"))
        return render_template('index.html', op="static/images/output.png")
    else:
        return render_template('index.html', op=None)
   

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

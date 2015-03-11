"""
2015/03/07
Nikkei x Cookpad Hackathon
Nikpad Application
"""
import os
import json
import random
import numpy
from flask import Flask
from flask import render_template, send_from_directory, Response, url_for, request

from dataloader import load_all

# app initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = '9c35679705479a2efd642954fdbd8943c5626f626bfb8c21'
)

# data initialization
NAMES = []
NODE_SIZES = []
NODE_LINKS = []
load_all(NAMES, NODE_SIZES, 50)

# controllers

@app.route('/')
def wheel():
    """ Our main function """

    random.seed()
    # NAMES = [\
    #   "Joshuaaaaaaaaa", "Daniel", "Robert", "Noah", "Anthony",\
    #   "Elizabeth", "Addison", "Alexis", "Ella", "Samantha",\
    #   "Joseph", "Scott", "James", "Ryan", "Benjamin",\
    #   "Walter", "Gabriel", "Christian", "Nathan", "Simon",\
    #   "Isabella", "Emma", "Olivia", "Sophia", "Ava",\
    #   "Emily", "Madison", "Tina", "Elena", "Mia",\
    #   "Jacob", "Ethan", "Michael", "Alexander", "William",\
    #   "Natalie", "Grace", "Lily", "Alyssa", "Ashley",\
    #   "Sarah", "Taylor", "Hannah", "Brianna", "Hailey",\
    #   "Christopher", "Aiden", "Matthew", "David", "Andrew",\
    #   "Kaylee", "Juliana", "Leah", "Anna", "Allison",\
    #   "John", "Samuel", "Tyler", "Dylan", "Jonathan",\
    # ]
    # random.random()
    # random.randint(a,b)
    N = len(NAMES)
    # NODE_SIZES = []
    NODE_CATEGORIES = []

    for i in range(N):
        # NODE_SIZES.append( random.random() )
        NODE_CATEGORIES.append( random.randint( 0, 7 ) )
        for j in range(N):
            NODE_LINKS.append( random.randint(0, 20) )

    print("ok")
    coded_names = '['
    coded_names += ','.join(NAMES)
    coded_names += ']'
    return render_template('amoeba.html', NAMES=coded_names,\
                NODE_SIZES=NODE_SIZES, NODE_CATEGORIES=NODE_CATEGORIES,\
                           NODE_LINKS=NODE_LINKS)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/test')
def test():
    return render_template('amoeba.html')

# special file handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

### static file helpers
# route for static js, css files
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)
@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)
@app.route('/font-awesome/<path:path>')
def send_fontawesome(path):
    return send_from_directory('static/font-awesome', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)
@app.route('/less/<path:path>')
def send_less(path):
    return send_from_directory('static/less', path)
@app.route('/skin/<path:path>')
def send_skin(path):
    return send_from_directory('static/skin', path)

# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# server launchpad
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

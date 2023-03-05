# imports
from flask import Flask,g,redirect,render_template,request,session
from flask_compress import Compress
from pymongo import MongoClient
from dotenv import load_dotenv
from login import main_login
from custom_modules import disablelog, time_format, slug
import json
import os
from datetime import timedelta

# fuck control c
import signal
import sys
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

# setup flask and important stuff
app = Flask(__name__)
# gzip for the rescue
Compress(app)
load_dotenv()
app.secret_key = os.urandom(24)

# variables
host = os.getenv('MONGODB')
port = os.getenv('PORT')
debug = os.getenv('DEBUG')
client = MongoClient(host, 27017)
db = client.blog
posts = db.posts

# index
@app.route('/')
def index():
    wut = 1
    # do not add posts.find() as a var, we need realtime update
    postfind = posts.find().sort("_id", -1).limit(10)
    return render_template('index.html', post=postfind, county=posts.count_documents({}), wut=wut)

# next page
@app.route('/<int:wut>')
def nextpage(wut):
    county = posts.count_documents({})
    mathy = county - (10 * (wut + 1))
    jesus = list(str(mathy))[0]
    # do not add posts.find() as a var, we need realtime update
    postfind = posts.find().sort("_id", -1).limit(10).skip(10 * wut)
    return render_template('index.html', post=postfind, county=county, wut=wut, jesus=jesus)

# display post
@app.route('/<pee>', methods=['GET','POST'])
def postsy(pee):
    if pee == "":
        return redirect('/blog', code=302)
    if request.method == "POST":
        id_comment = request.form['id_comment']
        posts.update_one({ "slug": id_comment },{ "$push": { "comments": {
            "name": request.form['username'],
            "content": request.form['content']
        }}})
        return redirect('/blog/' + id_comment)
    onepost = posts.find_one({"slug": pee})
    if onepost is None:
        return redirect('/blog', code=302)
    else:
        comments = posts.find_one({"slug": pee})['comments']
        return render_template('post.html', 
                            singlepost=onepost, 
                            comments=comments, 
                            numberofcomments=len(posts.find_one({"slug": pee})['comments']))

# fucking login stuff
@app.before_request
def before_request():
    g.user = None
    session.permanent = True
    if 'user_id' in session:
        user = [x for x in main_login.users if x.id == session['user_id']][0]
        g.user = user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in main_login.users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect('/blog/dashboard')

        return redirect('/blog/login')
    if g.user:
        return redirect('/blog/dashboard')
    return render_template('handle/login.html')

# create post
@app.route('/create', methods=['POST', 'GET'])
def create():
    if not g.user:
        return redirect('/blog/login')
    if request.method == "POST":
        noice = slug.gen(request.form['title'])
        pastn = noice
        posts.insert_one({
            "title": request.form['title'],
            "date": time_format.getdate(),
            "content": request.form['content'],
            "slug": pastn,
            "comments": [],
        })
        return redirect(pastn)
    return render_template('handle/add.html')

# dashboard
@app.route('/dashboard')
def profile():
    if not g.user:
        return redirect('/blog/login')
    return render_template('handle/dashboard.html')

@app.route('/manage')
def manage():
    if not g.user:
        return redirect('/blog/login')
    return render_template('handle/manage.html')

# nooooooooo
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/blog/login')

# FIRE THIS BITCH
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=debug, threaded=True)
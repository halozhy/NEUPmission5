
from flask import Flask, render_template, request, redirect, url_for
import time
app = Flask(__name__)

data = [{"text": "test","user": "root","date": "2019-10-19 04:41:47"},
        {"text": "2333","user": "halo","date": "2019-10-19 04:41:54"},
        {"text": "2333333","user": "halo","date": "2019-10-19 04:42:02"},
        {"text": "continue test","user": "root","date": "2019-10-19 04:42:15"},
        {"text": "666666","user": "halo","date": "2019-10-19 04:42:23"},
        {"text": "test2","user": "root","date": "2019-10-19 04:42:54"},
        {"text": "test3","user": "root","date": "2019-10-19 04:44:07"},
        {"text": "test4","user": "root","date": "2019-10-19 04:44:54"},
        {"text": "test5","user": "root","date": "2019-10-19 04:46:15"},
        {"text": "test6","user": "root","date": "2019-10-19 04:46:59"},
        {"text": "test7","user": "root","date": "2019-10-19 04:48:25"}]

# from app import app,render_template

@app.route('/',methods=['GET', 'POST'])
def board(): 
    if request.method=='GET':
        return render_template('board.html',d=data)
    elif request.method=='POST':
        text = request.form.get('text')
        user = request.form.get('user')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        if text != '' and user != '':
            data.append({"text": text,"user": user,"date": date})
        else:
            print("NULL info")
        return redirect(url_for('board'))
        
@app.route('/about',methods=['GET'])
def about(): 
    if request.method=='GET':
        return render_template('about.html')
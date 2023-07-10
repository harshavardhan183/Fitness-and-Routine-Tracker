from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import matplotlib.pyplot as plt


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trackers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




class Tracker(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Tracker = db.Column(db.String(200), nullable = False)
    Description = db.Column(db.String(500))
    tracker_type = db.Column(db.String(50))
    Last_modified = db.Column(db.DateTime, default = datetime.utcnow)


class Log(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    tracker_id = db.Column(db.Integer)
    time = db.Column(db.DateTime, default = datetime.utcnow)
    value = db.Column(db.String(50), nullable = False)
    Description = db.Column(db.String(200))



#####     TRACKERS ROUTES     #####
@app.route('/', methods = ['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if(email == "admin@gmail.com" and password == "admin"):
            allTrackers = Tracker.query.all()
            return render_template('index.html', allTrackers = allTrackers)
        
    return render_template('login.html')

@app.route('/index', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        tracker_name = request.form['tracker']
        description = request.form['desc']
        tracker_type = request.form['type']
        tracker = Tracker(Tracker = tracker_name, Description = description, tracker_type = tracker_type )
        db.session.add(tracker)
        db.session.commit()

    allTrackers = Tracker.query.all()
    return render_template('index.html', allTrackers = allTrackers)

@app.route('/Delete/<int:sno>')
def delete(sno):
    tracker = Tracker.query.filter_by(sno = sno).first()
    db.session.delete(tracker)
    db.session.commit()
    return redirect("/index")

@app.route('/Edit/<int:sno>', methods = ['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        tracker = Tracker.query.filter_by(sno = sno).first()
        tracker_name = request.form['tracker']
        desc = request.form['desc']
        tracker.Tracker = tracker_name 
        tracker.Description = desc
        db.session.add(tracker)
        db.session.commit()
        return redirect('/index')

    tracker = Tracker.query.filter_by(sno = sno).first()    
    return render_template('edit.html', tracker = tracker)



#####    LOGS ROUTES   #####

@app.route('/add_log_page/<int:sno>', methods = ['GET', 'POST'])
def add_log_page2(sno): 
    tracker = Tracker.query.filter_by(sno = sno).first()
    if request.method == "POST":
        log_value = request.form['value']
        log_desc= request.form['desc']
        log_tracker_id = sno
        log = Log(value = log_value, Description = log_desc, tracker_id = log_tracker_id)
        db.session.add(log)
        db.session.commit()
    
    allLogs = Log.query.all()
    # ## graph code beginning
    # x = []
    # y = []
    # for log in allLogs:
    #     if(log.tracker_id == tracker.sno):
    #         x.append(log.time)
    #         y.append(log.value)
    # plt.xlabel('Date&Time')
    # plt.ylabel(tracker.Tracker)
    # plt.plot(x,y)
    # plt.savefig('./static/images/graph.png')
    # ## graph code end
    return render_template('view_log_page.html', allLogs = allLogs, tracker = tracker)


@app.route('/Edit_log/<int:sno>', methods = ['GET', 'POST'])
def edit_log(sno):
    log = Log.query.filter_by(sno = sno).first() 
    sno = log.tracker_id
    tracker = Tracker.query.filter_by(sno = sno).first()
    if request.method == 'POST':
        log_value = request.form['value']
        log_desc = request.form['desc']
        log.value = log_value 
        log.Description = log_desc
        db.session.add(log)
        db.session.commit()
        s = "/add_log_page/" + str(sno)
        return redirect(s)
   
    return render_template('edit_log.html', log = log, tracker = tracker)

@app.route('/Delete_log/<int:sno>')
def delete_log(sno):
    log = Log.query.filter_by(sno = sno).first()
    sno = log.tracker_id
    db.session.delete(log)
    db.session.commit()
    return redirect("/add_log_page/"+str(sno))



if __name__ == "__main__":
    app.run(debug = True, port = 8000)
    db.create_all()
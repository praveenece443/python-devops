from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myapp.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Myapp(db.Model):
    cid = db.Column(db.Integer, primary_key = True)
    c_name = db.Column(db.String(500))

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {"Message": "Welcome to my Flask Login Page !!"}


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    #if request.method == 'POST':
    c_name = request.form.get("c_name")
    name = Myapp(c_name=c_name)
    db.session.add(name)
    db.session.commit()        
    return redirect(url_for('home1'))
    #else:
        #return render_template("dbbase.html")

@app.route('/delete/<int:cid>')
def delete(cid):
    name = Myapp.query.filter_by(cid = cid).first()
    deleted_name = name.c_name
    db.session.delete(name)
    db.session.commit()
    return redirect(url_for("home1", x = deleted_name))

@app.route("/dbbase")
def home1():
    my_list = Myapp.query.all()
    deleted_cname = request.args.get("x")
    return render_template("dbbase.html", l1=my_list, deleted_cname = deleted_cname)

if __name__ == '__main__':
    app.run()
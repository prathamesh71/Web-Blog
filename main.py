from flask import *
from function import *
one=Flask(__name__)
@one.route('/')
def home():
    return render_template('home.html')
@one.route('/registerasauthor')
def regauth():
    return render_template('regauth.html')
@one.route('/registerasuser')
def reguser():
    return render_template('reguser.html')
@one.route('/loginasauthor')
def logauth():
    return render_template('loginauthor.html')
@one.route('/loginasuser')
def loguser():
    return render_template('loginuser.html')
@one.route('/authorpage')
def authpage():
    return render_template('authorpage.html')
@one.route('/addblog')
def addblog():
    return render_template('addblog.html')
@one.route('/userpage')
def userpage():
    return render_template('userpage.html')
@one.route('/viewblog')
def view():
    x=showall()
    return render_template('viewpost.html', y=x)
@one.route('/loginauthor', methods=['post'])
def loginauthor():
    email=request.form['email']
    password=request.form['password']
    t=(email,password)
    t1=logdetailsauth(t)
    if t in t1:
        return redirect('/authorpage')
    else:
        return redirect('/loginasauthor')
@one.route('/loginuser', methods=['post'])
def loginuser():
    email=request.form['email']
    password=request.form['password']
    t=(email,password)
    t1=logdetailsuser(t)
    if t in t1:
        return redirect('/userpage')
    else:
        return redirect('/loginasuser')
@one.route('/addauth', methods=['post'])
def registerauthor():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    t=(name,email,password)
    addregauth(t)
    return redirect('/')
@one.route('/adduser', methods=['post'])
def registeruser():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    t=(name,email,password)
    addreguser(t)
    return redirect('/')
@one.route('/addblogpost', methods=['post'])
def addblogpost():
    name=request.form['name']
    title=request.form['title']
    blog=request.form['blog']
    t=(name,title,blog)
    newblog(t)
    return redirect('/authorpage') 
if __name__=='__main__':
    one.run(debug=True)
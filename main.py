<<<<<<< HEAD
from flask import Flask, request, redirect, render_template, session,flash
from flask_sqlalchemy import SQLAlchemy
import string
import os
from hashutils import make_pwd_hash, check_pwd_hash


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:bMhUHuSUthRMLp6Y@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

app.secret_key='launchcode'

=======
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import string

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:BuEt9t52PFgZIN72@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

>>>>>>> 83ddc26d2610cbbd3d85de82461fb97d94621a8a
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body=db.Column(db.String(1000))
<<<<<<< HEAD
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, title, body,owner):
        self.title=title
        self.body=body
        self.owner=owner
        

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(120))
    blogs = db.relationship('Blog', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pwd_hash(password)     

@app.route('/', methods=['GET'])
def index():
    all_users=User.query.all()
    return render_template('index.html',all_users=all_users)

@app.route('/blog', methods=['POST', 'GET'])
def blog():
    blog_id=request.args.get('id')
    user_id=request.args.get('user')
    
    if blog_id:
        blog_entry=Blog.query.get(blog_id)
        return render_template('blog_entry.html', blog_entry=blog_entry)
    
    if user_id:
        user_entry=User.query.get(user_id)
        return render_template("singleuser.html",user=user_entry)

    new_post = Blog.query.all()
    return render_template('blog.html', new_post=new_post)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error=''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and pw_hash == check_pwd_hash(password, user.pw_hash):
            session['username'] = username
            flash("Logged in", "success")
            return redirect('/newpost')

        if user and pw_hash != check_pwd_hash(password, user.pw_hash):
            error="password error"
            return render_template("/login.html", error=error)

        if not user:
            error="user does not exist"
            return render_template("login.html",error=error)

    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username=request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        
        print(password)
        print('*************')
        print('*************')
        print('*************')
        error=''
    
        if username == '':
            error='Please enter a username'

        if password == '' or verify == '':
            error = 'Please enter a Password'

        if password != verify:
            error = 'Passwords do not match'
            
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error= 'Username already exists. Please use another one!'
        
        if len(username)<3 or len(password)<3:
            error="Please enter a username and password that is longer than 3 characters"


        if not existing_user and not error:
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            return redirect('/newpost')
        
        else:
            return render_template('signup.html', username=username, error=error)
      
    return render_template('signup.html')

@app.before_request
def require_login():
    allowed_routes = ['login', 'blog', 'index', 'signup']        
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')
=======
    
    def __init__(self, title, body):
        self.title=title
        self.body=body
    

@app.route('/blog', methods=['POST', 'GET'])
def index():
    blog_id=request.args.get('id')
    if blog_id == None:
        new_post = Blog.query.all()
        return render_template('blog.html',title="Add a Blog Entry", new_post=new_post)
    else: 
        blog_entry=Blog.query.get(blog_id)
        return render_template('blog_entry.html', blog_entry=blog_entry)
>>>>>>> 83ddc26d2610cbbd3d85de82461fb97d94621a8a


@app.route('/newpost', methods=['POST', 'GET'])
def newpost(): 
    if request.method == "GET":
        return render_template('newpost.html') 
        
    if request.method == "POST":    
        title = request.form['title']
        body = request.form['body']

        title_error=''
        body_error=''
    
        if len(title) is 0: title_error="Please enter an input"    
        if len(body) is 0: body_error="Please enter an input"
        
        if title_error or body_error:    
<<<<<<< HEAD
            return render_template("newpost.html", title_error=title_error, body_error=body_error)
        
        if not title_error and not body_error:
            username= session['username']
            user=User.query.filter_by(username=session['username']).first()
            new_blog = Blog(request.form['title'], request.form['body'],user)
            db.session.add(new_blog)
            db.session.commit()    
            return redirect('/blog?id='+str(new_blog.id))
        else:
            return render_template("newpost.html", title_error=title_error, body_error=body_error)

@app.route('/blog_entry', methods=['POST'])
def blog_entry(): 
    current_user=User.query.filter_by(username=session['username']).first()
    blog.id=request.args.get('id')
    if request.method == "POST":
        return redirect('./blog?id={{new_blog.id}}', title=new_blog.title, body=new_blog.body, owner_id=current_user.username)



@app.route('/logout')
def logout(): 
    del session['username']
    return redirect('/blog')
=======
            return render_template("newpost.html", title=title, title_error=title_error, body=body, body_error=body_error)
        
        if not title_error and not body_error:
            new_blog=Blog(request.form['title'], request.form['body'])
            db.session.add(new_blog)
            db.session.commit()    
            return redirect('/blog')

@app.route('/blog_entry', methods=['POST'])
def blog_entry(): 
     blog_id=request.args.get('id')
     if request.method == "POST":
         redirect('./blog?id={{Blog.id}}')
>>>>>>> 83ddc26d2610cbbd3d85de82461fb97d94621a8a

if __name__ == '__main__':
    app.run()
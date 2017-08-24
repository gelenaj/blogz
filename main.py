from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import string

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:BuEt9t52PFgZIN72@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body=db.Column(db.String(1000))
    
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

if __name__ == '__main__':
    app.run()
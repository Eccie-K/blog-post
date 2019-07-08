from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class Quotes:
    '''
    Quote class to define quote Objects
    '''

    def __init__(self,id,author,quote,permalink):
        self.id =id
        self.author = author
        self.quote = quote
        self.permalink = permalink


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog',backref = 'user',lazy = 'dynamic')
    comments = db.relationship('Comments',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'    


class Blog(db.Model):
     __tablename__ = 'blogs'

     id = db.Column(db.Integer,primary_key = True)
     blog  = db.Column(db.String(255))
     blog_content = db.Column(db.String(5000))
     blog_category =  db.Column(db.String(255))
     users_id = db.Column(db.Integer,db.ForeignKey("users.id"))
     likes = db.Column(db.Integer)
     dislikes = db.Column(db.Integer)
     comments = db.relationship('Comments',backref =  'blog_id',lazy = "dynamic")

     def save_blog(self):
         db.session.add(self)
         db.session.commit()

     @classmethod
     def get_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog
     
     @classmethod
     def get_blogs(cls,blog_category):
        blogs = Blog.query.filter_by(blog_category = blog_category).all()
        return blogs


class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String())
    blog = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog):
        comments = Comments.query.filter_by(blog_id = blog).all()
        return comments  

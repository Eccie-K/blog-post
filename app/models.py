from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    blogs = db.relationship('Blog',backref = 'user',lazy = 'dynamic')

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
     blog_content = db.Column(db.String())
     blog_category =  db.Column(db.String(255))
     users_id = db.Column(db.Integer,db.ForeignKey("users.id"))
     upvotes = db.Column(db.Integer)
     downvotes = db.Column(db.Integer)

     def save_blog(self):
         db.session.add(self)
         db.session.commit()

     @classmethod
     def get_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog
     
     @classmethod
     def get_blogs(cls,pitch_category):
        pitches = Pitch.query.filter_by(blog_category=pitch_category).all()
        return blogs
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Comments,Quotes
from .forms import BlogForm, UpdateProfile,CommentsForm
from .. import db,photos
from ..requests import get_quote



@main.route('/')
def index():

    '''
    function to display blog categories
    '''
    #Getting pitches from different categories
    blogs_blogs = Blog.get_blogs('blogs')
    quote = get_quote()
    

    
   
    return render_template('index.html',blogs = blogs_blogs,quote = quote)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
    

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = form.blog.data
        category = form.category.data
        new_blog = Blog(blog_content = blog,blog_category = category,user = current_user, likes=0, dislikes=0)
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'Create Blog'
    return render_template('create_blog.html',title = title, blog_form = form)

@main.route('/blog/<int:id>', methods = ['GET','POST'])
def blog(id):
    blog = Blog.get_blog(id)
    

    if request.args.get("likes"):
        blog.likes += 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id)) 

    elif request.args.get("dislikes"):
        blog.dislikes += 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    comment_form = CommentsForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comments(comment = comment,user = current_user,blog_id = blog)
        

        new_comment.save_comment()
    comments = Comments.get_comments(blog)

    return render_template("blog.html", blog = blog, comment_form = comment_form, comments = comments)





@main.route('/blog/update/<int:id>', methods = ['GET','POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog.author != current_user:
        abort(403)
        form = BlogForm()
        if form.validate_on_submit():
            blog.title = form.title.data
            blog.content = form.content.data

            db.session.commit()
            flash ('your post has been updated','success')

            return redirect(url_for('blog',blog_id = blog.id))
            
        elif request.method =='GET':
                form.title.data = blog.title
                form.content.data = blog.content 

        return render_template('create_blog.html',title = 'Update Blog', blog_form = form)

@main.route('/blog/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Blog.query.get_or_404(id)
    if blog.user != current_user:
        abort(403)
        db.session.delete(blog)
        db.session.commit()

        flash('Your blog has been deleted' 'success')

        return redirect(url_for('index'))
    return redirect(url_for('main.index'))









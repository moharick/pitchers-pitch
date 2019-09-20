from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User,Comment,Upvote,Downvote
from .forms import PitchForm, CommentForm, UpvoteForm
from flask.views import View,MethodView
from .. import db



@main.route('/', methods = ['GET','POST'])
def index():

    '''
    Root page functions that return the home page and its data
    '''
    pitch = Pitch.query.all()
    title = 'Welcome to Pitchers-pitch'
    interviewpitch = Pitch.query.filter_by(category = "interviewpitch").all()
    promotionpitch = Pitch.query.filter_by(category = "promotionpitch").all()
    businesspitch = Pitch.query.filter_by(category = "businesspitch").all()


    return render_template('index.html', title = title, pitch = pitch,  interviewpitch= interviewpitch, promotionpitch = promotionpitch, businesspitch = businesspitch )

@main.route('/home', methods = ['GET','POST'])
def home():

    '''
    Root page functions that return the home page and its data
    '''
    pitch = Pitch.query.all()
    title = 'Welcome to Pitchers-pitch'
    interviewpitch = Pitch.query.filter_by(category = "interviewpitch").all()
    promotionpitch = Pitch.query.filter_by(category = "promotionpitch").all()
    businesspitch = Pitch.query.filter_by(category = "businesspitch").all()

    return render_template('home.html', title = title, pitch = pitch,  interviewpitch= interviewpitch, promotionpitch = promotionpitch, businesspitch = businesspitch)

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()


        return redirect(url_for('main.index'))
    return render_template('pitches.html',form=form)




@main.route('/comment/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('main.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    print(all_comments)
    return render_template('comments.html', form = form, all_comments = all_comments, pitch = pitch )

    """ The above allows you to add a comment in all the categories of the different pitches"""

@main.route('/pitch/upvote/<int:id>/upvote', methods = ['GET', 'POST'])
@login_required
def like(id):
    get_pitches = Upvote.query_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for each_pitch in get_pitches:
        to_str = f'{each_pitch}'
        if valid_string == to_str:
            return redirect(url_for('main.home',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.home',id=id))





@main.route('/pitch/downvote/<int:id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(id):
    get_pitches = Downvote.query_downvotes(id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id= id)

    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==id).first():
        return  redirect(url_for('main.home'))


    new_downvote = Downvote(pitch_id=id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.home'))






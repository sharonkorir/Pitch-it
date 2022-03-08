from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch
from .forms import UpdateProfile, PitchForm
from .. import db, photos
from flask_login import login_required, current_user


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general = Pitch.query.filter_by(category = 'general').all()
    business = Pitch.query.filter_by(category = 'business/tech strt-up').all()
    books = Pitch.query.filter_by(category = 'books').all()
    pick_up = Pitch.query.filter_by(category = 'pick-up lines').all()
    dad_jokes = Pitch.query.filter_by(category = 'dad jokes').all()
    title = 'Home - Pitch it in sixty'
    return render_template('index.html', title = title, general = general, business = business, books = books, pick_up = pick_up, dad_jokes = dad_jokes)

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

@main.route('/create_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
  
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data
        user_id = current_user
        new_pitch = Pitch(title=title, content=content, category=category, user_id=current_user._get_current_object().id)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', pitch_form=form)
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

    title = 'Home - Pitch it in sixty'
    return render_template('index.html')

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
        new_pitch = Pitch(title, content, category, user_id)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    title = f'{new_pitch.title}'
    return render_template('new_pitch.html',title = title, pitch_form=form)
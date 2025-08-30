from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from config import *
from models import db, User, Announcement
from forms import AdForm, ResponseForm, LoginForm, EmailForm

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Serializer для токенов верификации
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Создание таблиц и дефолтного модератора
with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='moderator').first():
        mod = User(username='moderator')
        mod.set_password('password')  # Измените пароль!
        db.session.add(mod)
        db.session.commit()

class FlaskUser(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    if user:
        flask_user = FlaskUser()
        flask_user.id = user.id
        flask_user.role = user.role
        return flask_user
    return None

@app.route('/')
def index():
    ads = Announcement.query.filter_by(status='approved').all()
    form = EmailForm()
    # Показ popup если email не verified
    if 'verified_email' not in session:
        flash('Пожалуйста, подтвердите email для создания объявлений.')
    return render_template('index.html', ads=ads, form=form)

@app.route('/verify_email', methods=['GET', 'POST'])
def verify_email():
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        token = s.dumps(email, salt='email-confirm')
        msg = Message('Подтверждение email', recipients=[email])
        msg.body = f'Ваш код подтверждения: {token}\nСкопируйте этот код и вставьте его на сайте для подтверждения.'
        mail.send(msg)
        flash('Код подтверждения отправлен на ваш email.')
        return redirect(url_for('confirm_email_form'))
    return render_template('index.html', form=form)  # Popup в index

@app.route('/confirm_email_form', methods=['GET', 'POST'])
def confirm_email_form():
    if request.method == 'POST':
        token = request.form['token']
        try:
            email = s.loads(token, salt='email-confirm', max_age=3600)
            session['verified_email'] = email
            flash('Email подтвержден!')
            return redirect(url_for('index'))
        except SignatureExpired:
            flash('Код истек. Попробуйте снова.')
        except:
            flash('Неверный код.')
    return render_template('confirm.html')  # Отдельный шаблон для ввода кода

@app.route('/create_ad', methods=['GET', 'POST'])
def create_ad():
    if 'verified_email' not in session:
        flash('Подтвердите email сначала.')
        return redirect(url_for('index'))
    form = AdForm()
    if form.validate_on_submit():
        ad = Announcement(
            gender=form.gender.data, age=form.age.data, country=form.country.data,
            region=form.region.data, city=form.city.data, text=form.text.data,
            email=session['verified_email'], status='pending'
        )
        db.session.add(ad)
        db.session.commit()
        print(f"Объявление создано: ID={ad.id}, Статус={ad.status}, Email={ad.email}")  # Отладка
        flash('Объявление отправлено на модерацию.')
        return redirect(url_for('index'))
    return render_template('create_ad.html', form=form)

@app.route('/respond/<int:ad_id>', methods=['GET', 'POST'])
def respond(ad_id):
    ad = Announcement.query.get_or_404(ad_id)
    form = ResponseForm()
    if form.validate_on_submit():
        # Отправить email автору
        msg = Message('Новый ответ на ваше объявление', recipients=[ad.email])
        msg.body = f'Ответ: {form.text.data}\nОт: {form.email.data}'
        mail.send(msg)
        flash('Ответ отправлен.')
        return redirect(url_for('index'))
    return render_template('respond.html', ad=ad, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data) and user.role == 'moderator':
            flask_user = load_user(user.id)
            login_user(flask_user)
            return redirect(url_for('moderator_panel'))
        flash('Неверный логин/пароль.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/moderator', methods=['GET', 'POST'])
@login_required
def moderator_panel():
    if current_user.role != 'moderator':
        return redirect(url_for('index'))
    pending_ads = Announcement.query.filter_by(status='pending').all()
    print(f"Объявления на модерации: {[ad.id for ad in pending_ads]}")  # Отладка
    if request.method == 'POST':
        ad_id = request.form['ad_id']
        action = request.form['action']
        ad = Announcement.query.get(ad_id)
        if action == 'approve':
            ad.status = 'approved'
        elif action == 'reject':
            ad.status = 'rejected'
        db.session.commit()
        flash('Объявление обработано.')
    return render_template('moderator.html', ads=pending_ads)

if __name__ == '__main__':
    app.run(debug=True)
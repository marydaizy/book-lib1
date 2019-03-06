from flask import render_template, url_for, flash, redirect, request
from books import app, db, bcrypt
from books.forms import RegistrationForm, LoginForm,SearchForm
from books.models import Users, Books
from flask_login import login_user, current_user, logout_user, login_required




@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('search'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('search'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        search = form.search.data
        books = Books.query.filter((Books.isbn.contains(search)) | (Books.title.contains(search)) | (Books.author.contains(search)) | (Books.year.contains(search)))
        return render_template('search.html', books = books, form=form)
    books = Books.query.all()
    return render_template('search.html', books = books, form=form)
    

@app.route("/detail/<int:book_id>", methods=["GET", "POST"])
def detail(book_id):
    if current_user.is_authenticated:
        books=Books.query.filter_by(id=book_id).first()
        return render_template("detail.html", books=books, error_message="Please Login First", work="Login")
    


@app.route("/book/<int:book_id>", methods=['GET', 'POST'])
def book(book_id):
    books=Books.query.get_or_404(book_id)
    return render_template('detail.html', books=books, form=form)
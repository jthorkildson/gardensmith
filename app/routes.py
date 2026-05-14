from flask import redirect, render_template, url_for
from app import app
from app.forms import ContactForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/services')
def services():
    return render_template('services.html', title='Services')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process the form data (e.g., send an email, save to database)
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact Us', form=form)

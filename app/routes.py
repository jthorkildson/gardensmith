from app import app

@app.route('/')
@app.route('/index')
@app.route('/services')
@app.route('/contact')
def index():
    return "hello world"
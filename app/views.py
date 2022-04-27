from flask import render_template
from Watchlist import app


# Views
@app.route('/')
def index():
    """
    View root page. Returns the index page as its data
    :return:
    """
    return render_template('index.html')

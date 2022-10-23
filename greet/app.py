from flask import Flask 

app = Flask(__name__)

"""make route to respond 'welcome'"""
@app.route('/welcome')
def welcome():
    return "welcome"

"""make route to respond 'welcome back'"""
@app.route('/welcome/back')
def welcome_back():
    return "welcome back"


"""make route to respond 'welcome home'"""
@app.route('/welcome/home')
def welcome_home():
    return "welcome home"
    
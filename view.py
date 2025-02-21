from flask import render_template, redirect, url_for

from models import Person


def routes(app, db):


    #route to home page
    @app.route('/')
    def main():
        return render_template('main.html')

    @app.route('/signin')
    def signin():
        return render_template('signin.html')

    @app.route('/login')
    def login():
        return render_template('login.html')    

    @app.route('/aboutuspage')
    def aboutuspage():
        return render_template('aboutuspage.html')  # Make sure this HTML file exists in the templates folder
    
    @app.route('/adoptadog')
    def adoptadog():
        return render_template('adoptadog.html')  # Make sure this HTML file exists in the templates folder

    @app.route('/adoptacat')
    def adoptacat():
        return render_template('adoptacat.html')  # Make sure this HTML file exists in the templates folder
    
    @app.route('/idonate')
    def idonate():
        return render_template('idonate.html')  # Make sure this HTML file exists in the templates folder


    @app.route('/adoptioninfo')
    def adoptioninfo():
        return render_template('adoptioninfo.html')  # Make sure this HTML file exists in the templates folder

    @app.route('/blogpage')
    def blogpage():
        return render_template('blogpage.html')  # Make sure this HTML file exists in the templates folder


    @app.route('/contactus')
    def contactus():
        return render_template('contactus.html')  # Make sure this HTML file exists in the templates folder

    @app.route('/qr')
    def qr():
        return render_template('qr.html')  # Ensure you have a `qr.html` file in your templates folder




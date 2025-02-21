#this package is for creating a flask application for use


from flask import Flask

#ORM for database
from flask_sqlalchemy import SQLAlchemy

#used for migration of data 
from flask_migrate import Migrate

#instance of databasd
db = SQLAlchemy()



#this method/function return a  flask applicaiton 
def create_app():

    #here we are creating one flask app 
    flask_app = Flask(__name__)

    #here we are defining the path of our database( path where database table will be created)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'

    #redner templates
    from view import routes
    routes(flask_app, db)

    migrate = Migrate(flask_app, db)
    db.init_app(flask_app)



    return flask_app


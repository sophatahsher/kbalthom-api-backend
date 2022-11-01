import os
from flask import Flask
from applications.environment_config import EnvConfig
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

'''
|--------------------------------------------------------------------------
| DotEnv
|--------------------------------------------------------------------------
| Load env configuration
|
'''
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'kbalthom_db')
db = SQLAlchemy(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')

@app.cli.command('db_seed')
def db_seed():
    customer = Customer(first_name='Sophat',
                        last_name='Chhay',
                        email='sophat.chhay@gmail.com',
                        profile_photo='sophat.jpg')
    db.session.add(customer)

    user = User(first_name='Sophat',
                        last_name='Chhay',
                        email='sophat.chhay@gmail.com',
                        password='123456')
    db.session.add(user)
    db.session.commit()
    print('Database seeded!')

class User(db.Model):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Customer(db.Model):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    profile_photo = Column(String)


#-----------------------------------------------------------------------------------------------------------------------
# ServerEnv
#-----------------------------------------------------------------------------------------------------------------------
server_mode = os.getenv("FLASK_ENV")
config_env  = EnvConfig(server_mode)
app.config.from_object(config_env)
#-----------------------------------------------------------------------------------------------------------------------

@app.route('/')
def hello_world():
    return 'Hellow World!'

from routes.v1.route import *

'''
|-----------------------------------------------------------------------------------------------------------------------
| Start Running Application
|-----------------------------------------------------------------------------------------------------------------------
'''
'''
if __name__ == '__main__':

    print(config_env.HOST)
    app.run(host=config_env.HOST, port=config_env.PORT, debug=config_env.DEBUG)

    
    print(config_env.HOST)
    print(config_env.PORT)
    print(config_env.DEBUG)
    app.run(host=config_env.HOST, port=config_env.PORT, debug=config_env.DEBUG)
'''
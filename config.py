import os
DEBUG=True

SECRET_KEY=os.urandom(24)

DIALECT='mysql'
DRIVER='pymysql'
USERNAME='root'
PASSWORD='19951208'
HOST='localhost'
PORT='3306'
DATABASE='test'
SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS=False
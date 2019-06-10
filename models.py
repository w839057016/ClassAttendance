from exts import db

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.String(10),primary_key=True)
    password=db.Column(db.String(20),nullable=False)
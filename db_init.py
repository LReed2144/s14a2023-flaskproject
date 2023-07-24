from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)

postgres_connection_string = "postgresql://doadmin:AVNS_8l9GVHut1Gdw3ZxvSLB@db-postgresql-sfo3-s14a2023-do-user-14318939-0.b.db.ondigitalocean.com:25060/s14a2023?sslmode=require"
app.config["SQLALCHEMY_DATABASE_URI"] = postgres_connection_string

db.init_app(app)

class User(db.Model):
    email = db.Column(db.String)
    phonenumber = db.Column(db.String)
    updated_at = db.Column(db.String)
    status = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    
# class Order(db.Model):
#     id = db.Column(db.Integer)
#     item_name = db.Column(db.String)
#     item_count = db.Column(db.Integer)
#     total = db.Column(db.Integer)
#     user_id = db.Column(db.Integer)
    

#     def as_dict(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    with app.app_context():
        db.create_all()

       # Query the whole table
        Users = db.session.execute(db.select(User).order_by(User.email)).scalars()
    for u in Users:
        print(u.as_dict())
    print("==========After Select All 1===============")

    # Insert a new object
    user1 = User(
        username="username1",
        email="email1@example.com",
    )
    db.session.add(user1)
    db.session.commit()
    print("==========After Commit===============")
    # Query the whole table
    userList = db.session.execute(
        db.select(User).order_by(User.email)).scalars()
    for u in userList:
        print(u.as_dict())
    print("==========After Select All 2===============")
    # Query by id, a specific record
    id = 1
    user = db.get_or_404(User, id)
    print(user.as_dict())
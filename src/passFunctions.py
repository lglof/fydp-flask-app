from src import db
from src.models import User
from werkzeug.security import generate_password_hash

def createNewUser(userType, contents):
    #call rfid to get user info here
    newPassHash = generate_password_hash(contents['password'])
    newUser = User(friendly=contents['friendly'], password_hash=newPassHash, user_type=userType )
    try:
        db.session.add(newUser)
        db.session.commit()
    except: 
        print("an exception occured")
        return 0
    else:
        return 1

def deleteUser(idNo):
    user = User.query.filter_by(id=idNo).limit(1).all()[0]
    try:
        db.session.delete(user)
        db.session.commit()
    except:
        print('oops')
        return 0
    else:
        return 1

def verifyPassword(contents):
    user = User.query.filter_by(friendly=contents['friendly']).limit(1).all()
    return user[0].checkPassword(contents['password'])
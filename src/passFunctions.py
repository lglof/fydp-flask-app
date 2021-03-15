from src import db
from src.models import User
from werkzeug.security import generate_password_hash

def createNewUser(userType, contents):
    #call rfid to get user info here
    try:
        newPassHash = generate_password_hash(contents['password'])
        newUser = User(friendly=contents['friendly'], password_hash=newPassHash, user_type=userType)
        db.session.add(newUser)
        db.session.commit()
    except: 
        print("an exception occured")
        return 0
    else:
        return newUser.to_dict()

def deleteUser(idNo):
    try:
        user = User.query.filter_by(id=idNo).limit(1).all()[0]
        db.session.delete(user)
        db.session.commit()
    except:
        print('oops')
        return 0
    else:
        return 1

def verifyPassword(contents):
    user = User.query.filter_by(friendly=contents['friendly']).limit(1).all()
    if(len(user) == 0):
        return 'no users'
    else:
        return user[0].checkPassword(contents['password'])
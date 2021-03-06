from flask import jsonify
from src import app, interventionFunctions, passFunctions
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return 'hell wrld'

@app.route('/createEntry', methods=['POST'])
def createEntry():
    interventionFunctions.addIntervention(request.json)
    return request.json

@app.route('/getEntries/<num>', methods=['GET'])
def getEntries(num):
    interventions = interventionFunctions.viewInterventions(num)
    data = {
        'items': [item.to_dict() for item in interventions]
    }
    return data

@app.route('/deleteEntry/<id>', methods=['DELETE'])
def removeIntervention(id):
    interventionFunctions.deleteIntervention(id)
    return 'deleted'

@app.route('/verify', methods=['GET'])
def verify():
    if (passFunctions.verifyPassword(request.json)):
        print('true in route')
        return {"check": True}
    else:
        print('false in route')
        return {"check": False}

@app.route('/newUser/<userType>', methods=['POST'])
def newUser(userType):
    passFunctions.createNewUser(userType, request.json)
    return 'created'

@app.route('/deleteUser/<id>', methods=['DELETE'])
def deleteUser(id):
    passFunctions.deleteUser(id)
    return 'deleted'

@app.route('/edit/<id>', methods=['PATCH'])
def edit(id):
    return 'backburner'

@app.route('/filterTime', methods=['GET'])
def filterTime():
    return 'not done yet'

@app.route('/filterType/<type>', methods=['GET'])
def filterType(type):
    return 'oh no'
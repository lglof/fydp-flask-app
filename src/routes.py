from flask import jsonify
from src import app, interventionFunctions, passFunctions, demoFunctions
from flask import request, make_response
from flask_cors import CORS, cross_origin

@app.route('/')
@cross_origin()
def index():
    return 'hell wrld'

@app.route('/createEntry', methods=['POST'])
@cross_origin()
def createEntry():
    newIntervention = interventionFunctions.addIntervention(request.json)
    return newIntervention

@app.route('/getEntries/<num>', methods=['GET'])
@cross_origin()
def getEntries(num):
    interventions = interventionFunctions.viewInterventions(num)
    data = {
        'items': [item.to_dict() for item in interventions]
    }
    return data

@app.route('/deleteEntry/<id>', methods=['DELETE'])
@cross_origin()
def removeIntervention(id):
    interventionFunctions.deleteIntervention(id)
    return 'deleted'

@app.route('/verify', methods=['POST'])
@cross_origin()
def verify():
    check = passFunctions.verifyPassword(request.json)
    response = make_response({'check': check})
    return response

@app.route('/newUser/<userType>', methods=['POST'])
@cross_origin()
def newUser(userType):
    passFunctions.createNewUser(userType, request.json)
    return 'created'

@app.route('/deleteUser/<id>', methods=['DELETE'])
@cross_origin()
def deleteUser(id):
    passFunctions.deleteUser(id)
    return 'deleted'

@app.route('/addDemographics', methods=['POST'])
@cross_origin()
def addDemographics():
    newDemographics = demoFunctions.createNewDemographics(request.json)
    return newDemographics

@app.route('/getDemographics/<id>', methods=['GET'])
@cross_origin()
def getDemographics(id):
    demographicInfo = demoFunctions.getDemographics(id)
    return demographicInfo

@app.route('/batchDemographics/<num>', methods=['GET'])
@cross_origin()
def batchDemographics(num):
    demographics = demoFunctions.batchDemographics(num)
    return demographics

@app.route('/edit/<id>', methods=['PATCH'])
@cross_origin()
def edit(id):
    return 'backburner'

@app.route('/filterTime', methods=['GET'])
@cross_origin()
def filterTime():
    return 'not done yet'

@app.route('/filterType/<type>', methods=['GET'])
@cross_origin()
def filterType(type):
    return 'oh no'
from flask import jsonify
from src import app, interventionFunctions, passFunctions, demoFunctions
from flask import request, make_response
from flask_cors import CORS, cross_origin

@app.route('/index')
@cross_origin()
def index():
    return 'hell wrld'

@app.route('/createEntry', methods=['POST'])
@cross_origin()
def createEntry():
    newIntervention = interventionFunctions.addIntervention(request.json)
    if (newIntervention == 'error'):
        response = make_response({"error_message": "missing field in provided intervention"}, 400)
    else:
        response = make_response(newIntervention, 201)
    return response

@app.route('/getEntries/<num>/<id>', methods=['GET'])
@cross_origin()
def getEntries(num, id):
    interventions = interventionFunctions.viewInterventions(num, id)
    data = {
        'items': [item.to_dict() for item in interventions],
        'num_items': len(interventions)
    }
    response = make_response(data, 200)
    return response

@app.route('/deleteEntry/<id>', methods=['DELETE'])
@cross_origin()
def removeIntervention(id):
    success = interventionFunctions.deleteIntervention(id)
    if success == 0:
        response = make_response({"error_message": "id does not exist"}, 400)
    else:
        response = make_response("Success", 200)
    return response

@app.route('/verify', methods=['POST'])
@cross_origin()
def verify():
    check = passFunctions.verifyPassword(request.json)
    if check == 'no users':
        response = make_response({'error_message': check}, 404)
    else: 
        response = make_response({'check': check}, 200)
    return response

@app.route('/newUser/<userType>', methods=['POST'])
@cross_origin()
def newUser(userType):
    newUser = passFunctions.createNewUser(userType, request.json)
    if newUser == 0:
        response = make_response({"error_message": "missing field"}, 400)
    else:
        response = make_response(newUser, 201)
    return response

@app.route('/deleteUser/<id>', methods=['DELETE'])
@cross_origin()
def deleteUser(id):
    out = passFunctions.deleteUser(id)
    if out == 0: 
        response = make_response({"error_message": "no user with that id exists"}, 400)
    else:
        response = make_response({'status': 'deleted'}, 200)
    return response

@app.route('/addDemographics', methods=['POST'])
@cross_origin()
def addDemographics():
    newDemographics = demoFunctions.createNewDemographics(request.json)
    if newDemographics == 0:
        response = make_response({"error_message": "Missing Key"}, 400)
    else: 
        response = make_response(newDemographics, 201)
    return response

@app.route('/getDemographics/<id>', methods=['GET'])
@cross_origin()
def getDemographics(id):
    demographicInfo = demoFunctions.getDemographics(id)
    if demographicInfo == 0:
        response = make_response({"error_message": "no patient with that id"}, 400)
    else:
        response = make_response(demographicInfo, 200) 
    return response

@app.route('/batchDemographics/<num>', methods=['GET'])
@cross_origin()
def batchDemographics(num):
    demographics = demoFunctions.batchDemographics(num)
    data = {
        'items': [item.to_dict() for item in demographics],
        'num_items': len(demographics)
    }
    response = make_response(data, 200)
    return response

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
from src import db
from src.models import Demographics

def createNewDemographics(contents):
    try:
        newDemographics = Demographics( \
            age=contents['age'], braden_score=contents['braden_score'], \
                diagnoses=contents['diagnoses'], medications=contents['medications'], \
                    patient=contents['patient'], prevention_plan=contents['prevention_plan'], \
                        room=contents['room'], most_recent=contents['most_recent'], \
                            mins_since_last=contents['mins_since_last'])
        db.session.add(newDemographics)
        db.session.commit()
    except:
        print('exception')
        return 0
    else:
        return newDemographics.to_dict()

def getDemographics(patientId):
    demographics = Demographics.query.filter_by(id=patientId).limit(1).all()
    if(len(demographics) == 0):
        return 0
    else:
        return demographics[0].to_dict()

def batchDemographics(num):
    demographics = Demographics.query.order_by(Demographics.mins_since_last.desc()).limit(num).all()
    return demographics
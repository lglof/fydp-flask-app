from datetime import datetime
from src import db
from src.models import PerformedIntervention, InterventionType

def addIntervention(contents):
    interventions = contents["interventions"]
    output = {}
    try:
        for intervention in interventions:
            newIntervention = PerformedIntervention()
            newIntervention.from_dict(intervention)
            db.session.add(newIntervention)
            db.session.commit()
            output["last_id"] = newIntervention.to_dict()["id"]
    except:
        print('an exception has occured')
        return 'error'
    else:
        output["num_interventions"] = len(interventions)
        return output

def viewInterventions(num, idNo):
    interventions = PerformedIntervention.query.filter_by(patient_id=idNo).order_by(PerformedIntervention.time.desc()).limit(num).all()
    return interventions

def deleteIntervention(idNo):
    intervention = PerformedIntervention.query.filter_by(id=idNo).limit(1).all()
    try:
        db.session.delete(intervention[0])
        db.session.commit()
    except:
        print('oops')
        return 0
    else:
        return 1
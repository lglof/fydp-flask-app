from src import db
from src.models import PerformedIntervention, InterventionType

def addIntervention(contents):
    newIntervention = PerformedIntervention( \
        type=contents['type'], worker=contents['worker'], \
             direction=contents['direction'], pain_level=contents['painLevel'])
    try:
        db.session.add(newIntervention)
        db.session.commit()
    except:
        print('an exception has occured')
        return 0
    else:
        return 1

def viewInterventions(num):
    interventions = PerformedIntervention.query.order_by(PerformedIntervention.time.desc()).limit(num).all()
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
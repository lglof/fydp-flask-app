# This will be for testing the demographics functions
# Corresponding routes: 
# addDemographics, getDemographics/<id>, batchDemographics/<num>

** Settings **
Library     RequestsLibrary
Library     Collections
Suite Setup  Create Session  SOAR  ${HOST}

** Variables ** 
&{HEADERS}  Accept=application/json    Content-Type=application/json    charset=utf-8
${HOST}  http://localhost:5000


** Test Cases **

addDemographics should return 201 ok when created
    &{good_demographics}=   Create Dictionary   age=92  braden_score=4  patient=test
...  room=room3  most_recent=shifting  last_intervention_time=1hr 17min  prevention_plan=data
...  diagnoses=data  medications=data  mins_since_last=12
    ${resp}=  POST On Session  SOAR  /addDemographics  json=&{good_demographics}  headers=&{HEADERS}
    Set Suite Variable  ${created_id}    ${resp.json()}[id]
    Status Should Be  201  ${resp}
    Dictionary Should Contain Key  ${resp.json()}  id

addDemographics should return 400 for incomplete data
    &{missing_demographics}=  Create Dictionary   age=92  braden_score=4  patient=test
...  room=room3  most_recent=shifting  last_intervention_time=1hr 17min  prevention_plan=data
...  diagnoses=data  medications=data
    ${resp}=  POST On Session  SOAR  /addDemographics  json=&{missing_demographics}  headers=&{HEADERS}  expected_status=anything
    Status Should Be  400  ${resp}
    Dictionary Should Contain Key  ${resp.json()}  error_message

getDemographics should return 200 and correct demographic info
    ${resp}=  GET On Session  SOAR  /getDemographics/${created_id}  headers=&{HEADERS}
    Status Should Be  200  ${resp}
    Dictionary Should Contain Key  ${resp.json()}  id

getDemographics should return 400 for id that doesn't exist
    ${resp}=  GET On Session  SOAR  /getDemographics/-1  headers=&{HEADERS}  expected_status=anything
    Status Should Be  400  ${resp}
    Dictionary Should Contain Key  ${resp.json()}  error_message

batchDemographics should return the right number of demographics
    Set Test Variable  ${expected_entries}  2
    ${resp}=  Get On Session  SOAR  /batchDemographics/${expected_entries}  headers=&{HEADERS}
    Status Should Be  200  ${resp}
    Should Be Equal As Strings  ${resp.json()}[num_items]  ${expected_entries}
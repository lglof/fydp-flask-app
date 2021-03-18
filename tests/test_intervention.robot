# this will be tests of the intervention functions

# Corresponding routes: 
# createEntry, getEntries/<num>/<id>, deleteEntry

** Settings **
Library     RequestsLibrary
Library     Collections
Suite Setup  Create Session  SOAR  ${HOST}

** Variables ** 
&{HEADERS}  Accept=application/json    Content-Type=application/json    charset=utf-8
${HOST}  http://localhost:5000

** Test Cases ** 

createEntry should return 201 ok and correct intervention summary
    &{intervention}=    Create Dictionary   type=1      worker=1   
...    direction=Left  painLevel=2    intervention_location=Left Elbow
...    pain_location=Right Elbow    pu_concern=1    late=1  patient_id=2
    &{data}=    Create Dictionary   interventions=[&{intervention}]
    ${resp}=    POST On Session   SOAR  /createEntry   json=&{data}     headers=&{HEADERS}
    Set Suite Variable   ${delete_id}    ${resp.json()}[last_id]
    Status Should Be    201     ${resp}
    Dictionary Should Contain Key  ${resp.json()}   num_interventions

deleteEntry should return 200 ok for id that exists
    ${resp}=    DELETE On Session  SOAR    /deleteEntry/${delete_id}  headers=&{HEADERS}  
    Status Should Be  200  ${resp}

deleteEntry should return 400 and error when id doesn't exist
    Set test variable  ${delete_incorrect_id}     -3
    ${resp}=    DELETE On Session   SOAR    /deleteEntry/${delete_incorrect_id}   headers=&{HEADERS}  expected_status=anything
    Status Should Be    400     ${resp}
    Dictionary Should Contain Key   ${resp.json()}     error_message

getEntries should return correct number of entries
    Set test variable  ${expected_entries}  2
    ${resp}=  Get On Session  SOAR  /getEntries/${expected_entries}/1  headers=&{HEADERS}
    Status Should Be    200     ${resp}
    Dictionary Should Contain Key  ${resp.json()}  items
    Should Be Equal As Strings  ${resp.json()}[num_items]  ${expected_entries}

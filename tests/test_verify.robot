# This will be for testing the verification functions
# Corresponding routes: 
# verify, newUser, DeleteUser

** Settings **
Library     RequestsLibrary
Library     Collections
Suite Setup  Create Session  SOAR  ${HOST}

** Variables ** 
&{HEADERS}  Accept=application/json    Content-Type=application/json    charset=utf-8
${HOST}  http://localhost:5000
&{NEW_USER}  friendly=test1   password=test2

** Test Cases **
newUser should return 201 ok for good username / password combo
    ${resp}=  POST On Session   SOAR    /newUser/test    json=&{NEW_USER}   headers=&{HEADERS}
    Set Suite Variable  ${created_id}    ${resp.json()}[id]
    Status Should Be    201     ${resp}
    Dictionary Should Contain Key  ${resp.json()}   id

newUser should return 400 for missing Key
    &{incomplete_user}=    Create Dictionary   friendly=test3
    ${resp}=    POST On Session     SOAR    /newUser/test   json=&{incomplete_user}    headers=&{HEADERS}  expected_status=anything
    Status Should Be    400     ${resp}
    Dictionary Should Contain Key   ${resp.json()}  error_message

verify should return true for correct user/password combo
    ${resp}=    POST On Session  SOAR    /verify     json=&{NEW_USER}    headers=&{HEADERS}
    Status Should Be    200  ${resp}
    Should Be Equal As Strings  ${resp.json()}[check]   True

verify should return false for incorrect user/password combo
    &{bad_password}=    Create Dictionary  friendly=test1   password=test4
    ${resp}=    POST On Session     SOAR    /verify     json=&{bad_password}    headers=&{HEADERS}
    Status Should Be  200   ${resp}
    Should Be Equal As Strings  ${resp.json()}[check]   False 

verify should return 404 for user not found
    &{bad_user}=    Create Dictionary   friendly=test5  password=test7
    ${resp}=    POST On Session     SOAR    /verify     json=&{bad_user}    headers=&{HEADERS}  expected_status=anything
    Status Should Be    404     ${resp}
    Dictionary Should Contain Key   ${resp.json()}  error_message

deleteUser should return 200 ok for good user id
    ${resp}=    DELETE On Session   SOAR    /deleteUser/${created_id}   headers=&{HEADERS}
    Status Should Be  200   ${resp} 

deleteUser should return 400 for non existent user id
    ${resp}=    DELETE On Session   SOAR    /deleteUser/-4      headers=&{HEADERS}  expected_status=anything
    Status Should Be    400  ${resp}
    Dictionary Should Contain Key  ${resp.json()}  error_message
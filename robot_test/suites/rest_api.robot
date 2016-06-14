*** Settings ***
Library  Process
Library  libs/RestApiKeywords.py
Test Setup  Start Flask App
Test Teardown  Stop Flask App


*** Variables ***
${APP_FILE}  rc_led_server.py
&{FLASK_ENV}  FLASK_APP=${CURDIR}/../../${APP_FILE}  FLASK_DEBUG=1


*** Keywords ***
Start Flask App
    ${handle}=  Start Process  /usr/local/bin/flask  run  env=&{FLASK_ENV}
    Sleep  1s
    Set Test Variable  ${PROCESS_HANDLE}  ${handle}

Stop Flask App
    Terminate Process  ${PROCESS_HANDLE}


*** Test Cases ***
First Meaningless Test
    When I try to issue a PUT API command with any kind of JSON info
    Then the server responds with a ACCEPT
    And the same information I have sent is echoed back to me

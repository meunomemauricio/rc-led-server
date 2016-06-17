*** Settings ***
Library  Process
Library  Selenium2Library
Library  libs/QRDecoder.py
Test Setup  Start Flask App and Browser
Test Teardown  Stop Flask App and Browser
Suite Setup  Open Browser  ${APP_URL}  browser=${BROWSER}
Suite Teardown  Close All Browsers
Force Tags  webserver


*** Variables ***
${APP_FILE}  rc_led_server.py
&{FLASK_ENV}  FLASK_APP=${CURDIR}/../../${APP_FILE}  FLASK_DEBUG=1

${APP_VERSION}  v0.1
${TITLE_SUFFIX}  - Remote LED Controller - ${APP_VERSION}

${APP_URL}  http://127.0.0.1:5000/rcled
${APP_TITLE}  Control Panel ${TITLE_SUFFIX}

${GEN_KEY_URL}  http://127.0.0.1:5000/rcled/generate_key
${GEN_KEY_TITLE}  Generate Key ${TITLE_SUFFIX}

${BROWSER}  firefox


*** Keywords ***
Start Flask App and Browser
    ${handle}=  Start Process  /usr/local/bin/flask  run  env=&{FLASK_ENV}
    Sleep  1s
    Set Test Variable  ${PROCESS_HANDLE}  ${handle}

Stop Flask App and Browser
    Terminate Process  ${PROCESS_HANDLE}

I change the page to the ${url}
    Go To  ${url}

the QR Code image is a valid QR Code
    ${element}=  Get Webelement  id=qrcode
    Check if an Image is a valid QR code  ${element}


*** Test Cases ***
Open the welcome page
    When I change the page to the ${APP_URL}
    Then Title Should Be  ${APP_TITLE}
    
Generate QR Code Key
    [Tags]  qrcode
    When I change the page to the ${GEN_KEY_URL}
    Then Page Should Contain Image  id=qrcode
    And Title Should Be  ${GEN_KEY_TITLE}
    And the QR Code image is a valid QR Code


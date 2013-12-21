*** Settings ***
Documentation   Common keywords and variables
Library         Selenium2Library
Library         custom_keywords.py


*** Variables ***
${SERVER}           http://localhost:9000
${BROWSER}          firefox
${SE_REMOTE_HUB}    http://127.0.0.1:4444/wd/hub
${LOGIN_URL}        ${SERVER}/login
${INBOX}       /tmp/test-mails



*** Keywords ***

Open Browser With Sentry
    Open Browser  ${SERVER}  ${BROWSER}  remote_url=${SE_REMOTE_HUB}
    Maximize Browser Window


Login As Admin
    Go To  ${LOGIN_URL}
    Input Text  username  admin
    Input Text  password  abc123
    Capture Page Screenshot
    Click Button  xpath=//button[@type="submit" and text()="Login"]


Go To Test Project Stream
    Go To  ${SERVER}/test-team/test-project/
    Wait Until Element Is Visible  xpath=//div[@id="event_list"]//ul[@class="group-list"]


Go To First Event
    Click Link  xpath=//div[@id="event_list"]//a[1]


Add Comment  [Arguments]  ${comment}
    Wait Until Element Is Visible  xpath=//textarea[@name="message"]
    Input Text  message  ${comment}

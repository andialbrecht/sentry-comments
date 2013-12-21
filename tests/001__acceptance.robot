*** Settings ***
Documentation       Acceptance tests
Resource            common.robot
Library             Selenium2Library
Suite Setup         Login As Admin


*** Test Cases ***

Comment Link Is Visible
    Go To Test Project Stream
    Go To First Event
    Page Should Contain Link  Comments
    Capture Page Screenshot


Add Comment On Test Event
    Go To Test Project Stream
    Go To First Event
    Clear Inbox  ${INBOX}
    Click Link  Comments
    Add Comment  This is a test comment.
    Click Button  Post comment
    Page Should Contain  This is a test comment.
    Page Should Contain Link  Comments (1)


Comment Count Is Updated On Event Page
    Go To Test Project Stream
    Go To First Event
    Page Should Contain Link  Comments (1)


Mail Should Be Sent
    Inbox Should Contain Num Mails  ${INBOX}  1
    Mail Should Contain Text  ${INBOX}  1  This is a test comment.
    Mail Should Contain Text  ${INBOX}  1  admin@example.com

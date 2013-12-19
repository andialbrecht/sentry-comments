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
    Click Link  Comments
    Input Text  message  This is a test comment.
    Click Button  Post comment
    Page Should Contain  This is a test comment.
    Page Should Contain Link  Comments (1)


Comment Count Is Updated On Event Page
    Go To Test Project Stream
    Go To First Event
    Page Should Contain Link  Comments (1)

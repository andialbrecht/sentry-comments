*** Settings ***
Documentation       Initializes a new Sentry instance with test data.
Resource            common.robot
Library             Selenium2Library
Suite Setup         Open Browser With Sentry


*** Test Cases ***

Login
    Login As Admin

Create Test Team
    Go To  ${SERVER}/account/teams/new/
    Input Text  name  Test Team
    Click Button  Create Team


Create Test Project
    Go To  ${SERVER}/account/teams/test-team/projects/new/
    Input Text  name  Test Project
    # we won't test Sentry itself, so just show that field :)
    Execute Javascript  $('#id_platform').show();
    Select From List By Value  id=id_platform  python
    Click Button  Save Changes
    Click Link  Settings
    Click Link  All Platforms
    ${dsn}=  Get Text  css=pre.clippy
    Set Global Variable  ${TEST_PROJECT_DSN}  ${dsn}
    Generate Event  Test Event 1  ${TEST_PROJECT_DSN}


Logout
    Go To  ${SERVER}/logout/

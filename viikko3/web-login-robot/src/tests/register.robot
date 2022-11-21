*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  nana
    Set Password  nana1234
    Set Password Confirmation  nana1234
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  na
    Set Password  nana1234
    Set Password Confirmation  nana1234
    Submit Register Credentials
    Register Should Fail With Message  Username must have min 3 characters

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  user
    Set Password  user123
    Set Password Confirmation  user123
    Submit Register Credentials
    Register Should Fail With Message  Password must have min 8 characters

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  tester
    Set Password  password123
    Set Password Confirmation  nomatch123
    Submit Register Credentials
    Register Should Fail With Message  Password and Password confirmation did not match 

Register Without Password Confirmation
    Go To Register Page
    Set Username  username
    Set Password  password123
    Submit Register Credentials
    Register Should Fail With Message  Password must be confirmed

Login After Successful Registration
    Go To Register Page
    Set Username  success
    Set Password  password123
    Set Password Confirmation  password123
    Submit Register Credentials
    Register Should Succeed
    Go to Login Page
    Set Username  success
    Set Password  password123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Go To Register Page
    Set Username  fail
    Set Password  password
    Set Password Confirmation  password
    Submit Register Credentials
    Register Should Fail With Message  Password must include min 1 number or special character
    Go to Login Page
    Set Username  fail
    Set Password  password
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

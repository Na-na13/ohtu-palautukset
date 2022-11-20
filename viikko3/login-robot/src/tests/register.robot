*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  nana  salasana2
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  na  salasana3
    Output Should Contain  Username must have min 3 characters

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  user  sala1
    Output Should Contain  Password must have min 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  user  salasana
    Output Should Contain  Password must include min 1 number or special character

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  nana  salasana1

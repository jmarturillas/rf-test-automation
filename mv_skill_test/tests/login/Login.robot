*** Settings ***
Library  Selenium2Library
Library  Login.py

Test Setup  run keyword  launch app
Test Teardown  run keyword  close browser


*** Test Cases ***
Validate Login With Empty Password Field
    [Documentation]  Validate webpage will return error behavior if any field in form is not filled.
    login with  username=music.acct91@gmail.com  password=
    validate error in page

Validate Login With Invalid Credentials
    [Documentation]  Validate webpage will return error behavior if incorrect credential was passed.
    login with  username=music.acct91@gmail.com  password=incorrect_password
    validate error in page

Validate Forgot Password Page
    [Documentation]  Validate that the forgot password page has email text field.
    click forgot password
    validate email text field in page

Validate Successful Login
    [Documentation]  Validate that main page displays after a successful login.
    login with  username=username=music.acct91@gmail.com  password=dummy1991
    validate redirect account home page
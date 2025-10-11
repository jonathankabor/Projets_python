*** Settings ***
Documentation   To validate the login form
Library    SeleniumLibrary
Test Setup      open the browser with the Mortgage payment url
Test Teardown   Close Browser session
Resource        resource.robot
#selenium


*** Variables ***
${LOGIN URL}  https://rahulshettyacademy.com/loginpagePractise/
${BROWSER}      chrome
${username}
${password}
${password1}
${Error_Message_Login}      css:.alert-danger
${element}                  css:.nav-link



*** Test Cases ***
Validate UnSuccesful Login

	    Submit Credentials
        verify error message is correct

Validate Cards display in the Shopping Page
        open the browser with the Mortgage payment url
	    Input Username      rahulshettyacademy
	    Input Password      learning
        Submit Credentials
        Wait Until Element Is Visible    ${element}


*** Keywords ***
open the browser with the Mortgage payment url
	 Open Browser   ${LOGIN URL}  ${BROWSER}

Input Username
	[Arguments]    ${username}
	Input Text          id:username     ${username}
Input Password
	[Arguments]    ${password1}
	Input Text           id:password     ${password1}
Submit Credentials
	Click Button    signInBtn

	Wait Until Element Is Visible    ${element}

Close Browser session
    Close Browser
















*** Settings ***
Documentation   To validate the login form
Library    SeleniumLibrary
Test Teardown   Close Browser
#Resource
#selenium

*** Variables ***
${LOGIN URL}  https://rahulshettyacademy.com/loginpagePractise/
${BROWSER}      chrome
${username}
${password}
${password1}    learning
${Error_Message_Login}      css:.alert-danger

*** Test Cases ***
Validate UnSuccesful Login
	   open the browser with the Mortgage payment url
	   Input Username   rahulshettyacademy
	   Input Password   12345678
	   Submit Credentials
	   #Fill the login form
	   #Wait Until Keyword Succeeds
	   verify error message is correct

*** Keywords ***
open the browser with the Mortgage payment url
	 Open Browser   ${LOGIN URL}  ${BROWSER}

Input Username
	    [Arguments]    ${username}
	    Input Text          id:username     ${username}
Input Password
	    [Arguments]    ${password}
        Input Text           id:password     ${password}
Submit Credentials
	    Click Button    signInBtn

	    Wait Until Element Is Visible    ${Error_Message_Login}

Verify error message is correct
	    ${result}=  Get Text    ${Error_Message_Login}

















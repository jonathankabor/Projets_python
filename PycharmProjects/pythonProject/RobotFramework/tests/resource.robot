*** Settings ***
Documentation   A resource file with reusable keywords and variables
...
...             The system specific keywords created here form our own
...             domain specific language. They utilize keywords provided
...             by the imported SeleniumLibrary.
Library         SeleniumLibrary
Library         OperatingSystem



*** Variables ***
${LOGIN URL}  https://rahulshettyacademy.com/loginpagePractise/
${BROWSER}      chrome
${username}     rahulshettyacademy
${password}     12345678
${password1}    learning
${Error_Message_Login}      css:.alert-danger
${element}                  a.nav-link.btn.btn-primary

*** Test Cases ***
Validate UnSuccesful Login

	   Input Username   rahulshettyacademy
	   Input Password   12345678
	   Submit Credentials
	   #Fill the login form
	   #Wait Until Keyword Succeeds
	   #Wait Until it checks and display error message
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

Close Browser session
    Close Browser
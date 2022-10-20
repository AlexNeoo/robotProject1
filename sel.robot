*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
LoginTest
   Given Open Browser   https://opensource-demo.orangehrmlive.com/   Chrome
   When Input Text  xpath=//*[@class='oxd-input oxd-input--active' and contains(text(),'username')]   Admin
   Then Sleep    5
   And  Close Browser




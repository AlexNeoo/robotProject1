*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
LoginTest
   Given Open Browser   https://opensource-demo.orangehrmlive.com/   Chrome
   When Input Text  xpath://*/input[@name='username']   Admin
   Then Sleep    5
   And  Close Browser




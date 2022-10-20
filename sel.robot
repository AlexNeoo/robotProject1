*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
LoginTest
   Given Open Browser   https://opensource-demo.orangehrmlive.com/   Chrome
   And Sleep    5
   When Click Button    xpath://*/button
   Then Sleep    5
   And Close Browser





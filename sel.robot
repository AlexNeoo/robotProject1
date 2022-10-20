*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
LoginTest
   Given Open Browser   https://opensource-demo.orangehrmlive.com/   Chrome
   Then Sleep    5
   When Click Button    xpath://*/button
   And Close Browser





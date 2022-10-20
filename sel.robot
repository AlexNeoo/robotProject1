*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
LoginTest
    Open Browser    https://opensource-demo.orangehrmlive.com/     Chrome
    Sleep    5
    Close Browser



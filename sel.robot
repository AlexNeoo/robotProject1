*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
LoginTest
   Given Open Browser    https://opensource-demo.orangehrmlive.com/     Chrome
   When Sleep    5
   Then Close Browser



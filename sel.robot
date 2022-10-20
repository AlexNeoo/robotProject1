*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
LoginTest
   Given Open Browser   https://opensource-demo.orangehrmlive.com/     Chrome
   When  Input Text     id=txtUsername                                 admin
   Then  Sleep    5
   And   Close Browser




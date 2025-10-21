*** Settings ***
Library           OperatingSystem
Library    SeleniumLibrary
Variables  ../resources/variables.py
Library    ../resources/CustomKeywords.py


*** Test Cases ***
Login And Logout
    Open Site
    Login To Site    ${login}   ${password}
    Logout From Site
    CustomKeywords.Close Browser

Login Buy And Logout
    Open Site
    Login To Site    ${login}    ${password}
    Add To Cart    ${productOne}
    Add To Cart    ${productTwo}
    Add To Cart    ${productThree}
    Buy Product From Site
    Logout From Site
    CustomKeywords.Close Browser

Sign Up New User And Login And Logout
    Open Site
    ${login}    ${password}=    Sign Up To Site
    Login To Site    ${login}    ${password}
    Logout From Site
    CustomKeywords.Close Browser


Sign Up New User And Login And Buy And Logout
    Open Site
    ${login}    ${password}=    Sign Up To Site
    Login To Site    ${login}    ${password}
    Add To Cart
    Buy Product From Site
    Logout From Site
    CustomKeywords.Close Browser



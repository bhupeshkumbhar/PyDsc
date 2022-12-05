import requests
from easygui import enterbox
from easygui import msgbox

def new_account():
    api_url = 'https://easy-authenticator.p.rapidapi.com/newAuthKey?'
    api_qry = {"account":"Yogesh.Shelar","issuer":"ZENCON"}
    api_hdr = {"X-Rapidapi-Key":"472f53a83bmsh0945009f2fe0c7bp1d4da4jsn137f40e946b5","X-RapidAPI-Host": "easy-authenticator.p.rapidapi.com"}

    response = requests.request("POST",api_url,headers=api_hdr,params=api_qry)
    print(response.json())

def auth_user():
    token = enterbox("Please enter Token")
    api_url = 'https://easy-authenticator.p.rapidapi.com/verify'
    api_qry = {"secretCode":"333K6O6QVP5SH7UR7JH7A6RGT3LZMWZB","token":token,"name":"bhupesh.kumbhar"}
    api_hdr = {"X-Rapidapi-Key":"472f53a83bmsh0945009f2fe0c7bp1d4da4jsn137f40e946b5","X-RapidAPI-Host": "easy-authenticator.p.rapidapi.com"}

    response = requests.request("POST",api_url,headers=api_hdr,params=api_qry)
    if response.json()["verify"]:
        msgbox("One Time Password is Correct","Message","Continue")
    else:
        msgbox("One Time Password is inCorrect","Message","Continue")
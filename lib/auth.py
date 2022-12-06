import sys,requests

def new_account():
    api_url = 'https://easy-authenticator.p.rapidapi.com/newAuthKey?'
    api_qry = {"account":"Yogesh.Shelar","issuer":"ZENCON"}
    api_hdr = {"X-Rapidapi-Key":"472f53a83bmsh0945009f2fe0c7bp1d4da4jsn137f40e946b5","X-RapidAPI-Host": "easy-authenticator.p.rapidapi.com"}

    response = requests.request("POST",api_url,headers=api_hdr,params=api_qry)
    print(response.json())

def auth_user(inp_data):
    usname = inp_data[0]
    secret = inp_data[1]
    gtoken = inp_data[2]

    api_url = 'https://easy-authenticator.p.rapidapi.com/verify'
    api_qry = {"secretCode":secret,"token":gtoken,"name":usname}
    api_hdr = {"X-Rapidapi-Key":"472f53a83bmsh0945009f2fe0c7bp1d4da4jsn137f40e946b5","X-RapidAPI-Host": "easy-authenticator.p.rapidapi.com"}

    api_rsp = requests.request("POST",api_url,headers=api_hdr,params=api_qry)

    if api_rsp.json()["verify"]:
        lv_resp = "True"
    else:
        lv_resp = "False"
    
    print(lv_resp)

    with open("resp.txt", "w") as resp:
        resp.write(lv_resp)







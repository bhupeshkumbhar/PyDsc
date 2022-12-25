import requests 

def company_details(inp_data):
    api_qurl = 'https://sandbox.surepass.io/api/v1/corporate/company-details'
    api_auth = 'Bearer '+ 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MTQyOTQxMSwianRpIjoiNjY5MjMzNzctNzA0YS00M2Y5LTg3NTItZTliZjU1MzBmYWE2IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiZGV2LnplbmNvbkBzdXJlcGFzcy5pbyIsIm5iZiI6MTY3MTQyOTQxMSwiZXhwIjoxNjcxOTQ3ODExLCJ1c2VyX2NsYWltcyI6eyJzY29wZXMiOlsid2FsbGV0Il19fQ.fIdxKwX33625N1WNKaqvOVWrjpelK9r6XHdWJkUKtWw'
    api_head = {
        'Authorization': api_auth,
        'Content-Type': 'application/json'
    }   
    api_body = { "id_number": "U74999PN2017PTC168776"}

    api_resp = requests.post(api_qurl,headers=api_head,json=api_body)

    print(api_resp.text)

inp_data={}
company_details(inp_data)


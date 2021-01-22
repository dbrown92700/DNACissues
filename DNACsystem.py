import requests
import base64
import sys

def getToken(baseurl, user, password):
    url = f"{baseurl}/dna/system/api/v1/auth/token"
    payload={}
    basicauth=f'{user}:{password}'
    b64auth = base64.b64encode(basicauth.encode('ascii')).decode('ascii')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {b64auth}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return response.text

if __name__ == '__main__':
    print(getToken(sys.argv[1],sys.argv[2],sys.argv[3]))

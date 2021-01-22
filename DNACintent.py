import requests
import sys

def getIssues(baseurl, token):

    url = f"{baseurl}/dna/intent/api/v1/issues"
    payload={}
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    return response.text

if __name__ == '__main__':
    print(getIssues(sys.argv[1],sys.argv[2]))
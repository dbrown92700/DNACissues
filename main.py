#!python3

from DNACsystem import getToken
from DNACintent import getIssues
from gmail import send_gmail, send_email
import json

from includes import baseurl, dnac_user, dnac_password, from_user, from_password, recipient, mail_server, mail_port

#
# Change the key above to issueId once defect CSCvw65555 is fixed in 2.1.2.6 or higher.
# Currently set to issue 'name'
#
key = 'name'

#
# Log into DNAC and pull current global issues list
#
token = json.loads(getToken(baseurl, dnac_user, dnac_password))['Token']
jissues = json.loads(getIssues(baseurl, token))

#
# Read previous global issues list from local file and save to set
#
oldissueset = set({})
infile = open('issueset.txt', 'r')
for lines in infile:
    oldissueset.add(lines.strip('\n'))
infile.close()

#
# Create new issues set and overwrite local file
# Add net new issues to an e-mail message
#
currentissueset = set({})
issue_count = 0
mail_body = ' new global issue(s) detected on DNA Center\n\n'
outfile = open('issueset.txt', 'w')
for issue in jissues['response']:
    currentissueset.add(issue[key])
    if issue[key] not in oldissueset:
        issue_count += 1
        mail_body += json.dumps(issue, indent=4).replace('"', '') + '\n'
    outfile.write(f"{issue[key]}\n")
outfile.close()
mail_body = str(issue_count) + mail_body

#
# calculate net new issues and send e-mail if new issues exist
#
newissues = currentissueset - oldissueset

if newissues == set({}):
    print('No new issues')
else:
    print('New Issues: ', newissues)
    if 'gmail.com' in from_user:
        send_gmail(gmail_user, gmail_password, recipient, 'THD DNAC Alert', mail_body)
    else:
        send_email(from_user, from_password, recipient, 'THD DNAC Alert', mail_body, mail_server, mail_port)

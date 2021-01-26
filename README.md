# DNAC Assurance Global Issues Alert

Reads global issues and sends an e-mail with any net new issues since the last run.

- Set DNAC host and credentials in includes.py.
- Needs a gmail account to send alerts.
- Gmail account has to have the "Less secure app access" setting enabled for this to work.  Recommend a dedicated account to avoid using low security on your account.
- Set gmail credentials in includes.py
- Execute python3 main.py

Recommend using your operating system scheduling tool to run this script periodically to inspect issues and generate an email alerts.

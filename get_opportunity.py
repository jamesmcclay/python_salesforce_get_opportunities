import simple_salesforce as ss
from random import randint

sf = ss.Salesforce(
        username='user@example.com',
        password='SuperSecret',
        instance_url='https://automationjamescom-dev-ed.my.salesforce.com/', 
        security_token='MyToken'
        )

q = sf.query('SELECT Id, Name FROM Account')
selection = randint(0,len(q['records']) - 1 )
account = q['records'][selection]

print(f"Working with account: {account['Name']}")

q2 = sf.query(f"SELECT Id, Name FROM Opportunity WHERE Account.Id = '{account['Id']}'")

print(f"Working with opportunity: {q2['records'][0]['Name']}")

opp = sf.Opportunity.get(q2['records'][0]['Id'])

info = f"""
Stage: {opp['StageName']}
Fisacal Year: {opp['FiscalYear']}
Amount: {opp['Amount']}
Probability: {opp['Probability']}
"""
print(info)





from exchangelib import DELEGATE, Account, Credentials

creds = Credentials(
    username='MYWINDOMAIN\myusername', 
    password='topsecret')
account = Account(
    primary_smtp_address='john@example.com',
    credentials=creds, 
    autodiscover=True, 
    access_type=DELEGATE)

# Print first 100 inbox messages in reverse order
for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.body, item.attachments)
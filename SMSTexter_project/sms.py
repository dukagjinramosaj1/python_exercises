# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = #GENERATED FROM TWIL.IO'
auth_token = #GENERATED FROM TWIL.IO'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='I CANT BELIEVE THIS WORKS ! !',
                              from_=#'your number',
                              to=#'Receipent's number'
                          )

print(message.sid)
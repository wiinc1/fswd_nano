from twilio.rest import TwilioRestClient

account_sid = "AC3e0efbf007c5858251eb1d25c8c1a797" # Your Account SID from www.twilio.com/console
auth_token  = "22b5b54fbe072638f416960d707105e4"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="My name is Ron Burdandy?",
    to="+13049865538",    # Replace with your phone number
    from_="+13045047054") # Replace with your Twilio number

print(message.sid)
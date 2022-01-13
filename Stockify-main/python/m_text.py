from twilio.rest import Client


def sendSMS(msg):
    account_sid = 'AC051523f83260cc5f2e3a1a262fd786dd'
    auth_token = '1294e6b9e75e3a5680c3d87bc9cb2ebc'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG40178e52cf212b0d144619b63b7fde9c',
        body=msg,
        to='+12265825700'
    )

    print(message.sid)

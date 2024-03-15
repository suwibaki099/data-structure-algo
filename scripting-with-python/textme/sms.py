from twilio.rest import Client

account_sid = 'AC74f4cdccaf9a825c05c177021257a3ab'
auth_token = '53074009932b33c8ee03b4f2c97b6a4d'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16592745249',
  body='test',
  to='+18777804236'
)

print(message.sid)

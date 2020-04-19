import time
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACac24aa4e1873f771a2090898cea22e24"
# Your Auth Token from twilio.com/console
auth_token  = "a581d8bfd5584c02fbc832685110e022"

client = Client(account_sid, auth_token)

datetime = "Sun Apr 19 22:36:00 2020"
while True:
    t = time.localtime()
    time.sleep(1)
    if time.asctime(t) == datetime:
        message = client.messages.create(
            to="+886911581183", 
            from_="+12029492754",
            body="Hello from Python!, 你的程式寫成功了!")
        print ("現在時間: %s , 已發送簡訊!" % time.asctime(t))
        print(message.sid)    
    else:
        print('預計發送簡訊時間為: ', datetime, ', 現在時間為: %s' % time.asctime(t))
import yagmail
import os
import time
from datetime import datetime as dt

sender= "pintilei92@gmail.com"
receiver= "	andreea.nanmarinescu@yahoo.com"
subject= "This is a great subject :D"

contents= "Not such a good content!"
while True: 
  now= dt.now()
  if now.hour == 19 and now.minute == 40:     # TIME Z
    yag= yagmail.SMTP(user= sender, password=os.environ['PASS'])
    yag.send(to= receiver, subject= subject, contents= contents)
    print("Email sent!")
    time.sleep(60)
    
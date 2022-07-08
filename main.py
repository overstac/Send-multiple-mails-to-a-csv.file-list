import yagmail
import os
import pandas
sender= "pintilei92@gmail.com"
subject= "Subiect"

df = pandas.read_csv("contacts.csv")

yag= yagmail.SMTP(user= sender, password=os.environ['PASS'])

for index, row in df.iterrows():
  contents= f"Hey there {row['name']} the content is nice !"
  yag.send(to= row["email"], subject= subject, contents= contents)
  print("Email sent!")    

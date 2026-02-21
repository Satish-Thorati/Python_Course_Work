#23. Message Sender

class Sender:
   def send(self):
       pass

class Email(Sender):
   def send(self):
       print("Sending Email...")

class SMS(Sender):
   def send(self):
       print("Sending SMS...")

def send_alert(obj):
   obj.send()

send_alert(Email())
send_alert(SMS())
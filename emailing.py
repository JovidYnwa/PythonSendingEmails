import smtplib
from email.message import EmailMessage
'''
In this file we configure our mailing modlule

'''

def email_customer(subject, body, to):
   msg = EmailMessage()
   msg.set_content(body)
   msg['subject'] = subject
   msg['to'] = to

   user = 'vendettaynwa@gmail.com'
   msg['from'] = user
   password = 'ardnnxypzwufxvqa'

   server = smtplib.SMTP("smtp.gmail.com", 587)
   server.starttls()
   server.login(user, password)
   server.send_message(msg)

   server.quit()
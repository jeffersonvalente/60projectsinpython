import smtplib 
import os
from email.message import EmailMessage

email_id =os.environ.get('EMAIL_ADDR')
email_pass =os.environ.get('EMAIL_PASS')

msg= EmailMessage()
msg['Subject'] = "um texto"
msg["From"] = email_id
msg["To"] = 'spam@gmail.com'
msg.set_content("bonito e inteligente poderia estar aqui, mas to com preguiça, mas ta feito")

with smtplib.SMTP_SSL('smtp.gmail.com',465)  as smtp:
    smtp.login(email_id,email_pass)
    smtp.send_message(msg)
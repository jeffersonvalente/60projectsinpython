import smtplib 
import os
import imghdr
from email.message import EmailMessage

email_id =os.environ.get('EMAIL_ADDR')
email_pass =os.environ.get('EMAIL_PASS')

msg= EmailMessage()
msg['Subject'] = "Vai ter foto"
msg["From"] = email_id
msg["To"] = 'spam@gmail.com'
msg.set_content("tem algo legal se abrir")

files = ["pikachu1.jpg","pikachu2.jpg"]
for file in files:
    with open (file,'rb') as m:
        file_data = m.read()
        file_type = imghdr.what(m.name)
        file_name = m.name

    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465)  as smtp:
    smtp.login(email_id,email_pass)
    smtp.send_message(msg)
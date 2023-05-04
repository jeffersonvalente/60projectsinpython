import smtplib 
import os

email_id =os.environ.get('EMAIL_ADDR')
email_pass =os.environ.get('EMAIL_PASS')
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_id,email_pass)
    
    subject = "um texto"
    body = "bonito e inteligente poderia estar aqui, mas to com preguiça"
    
    msg= f'Subject : {subject}\n\n\n{body}'
    smtp.sendmail(email_id,'spam@gmail.com', msg.encode('utf-8'))
#EMAIL SENDING
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = #'Your Name'
email['to'] = #'To recepient's address'
email['subject'] = 'You won 1,000,000 dollars'

 
email.set_content(html.substitute({'name': 'TinTin'}), 'html') 


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(#'e-mail ','password')
    smtp.send_message(email)
    print('All good boss!')


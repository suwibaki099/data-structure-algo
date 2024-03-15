import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Bbox Express'
email['to'] = 'aguilarandrea0004@gmail.com'
email['subject'] = 'this is a test!'

email.set_content(html.substitute(name='8234'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jandy.gulpe12@gmail.com', 'pvvpuhmvoygazpwq')
    smtp.send_message(email)
    print('all good boss!')

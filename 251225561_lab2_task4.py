import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import *
from base64 import *
import ssl

YOUR_EMAIL = 'saahash@gmail.com'
YOUR_PASSWORD = "gngpdxzgvzuodktn"
YOUR_DESTINATION_EMAIL = input("Enter Email Destination : ")
YOUR_SUBJECT_EMAIL = input("Enter Subject : ")
YOUR_BODY_EMAIL = input("Enter Message : ")

mailServer = 'smtp.gmail.com'
mailPort = 587

message = MIMEMultipart()
message['From'] = YOUR_EMAIL
message['To'] = YOUR_DESTINATION_EMAIL
message['Subject'] = YOUR_SUBJECT_EMAIL
message.attach(MIMEText(YOUR_BODY_EMAIL, 'plain'))

msg = '{}. \r\nI love computer networks!'.format(YOUR_BODY_EMAIL)
endmsg = '\r\n.\r\n'

session = smtplib.SMTP(mailServer, mailPort)
session.starttls()
session.login(YOUR_EMAIL, YOUR_PASSWORD)
text = message.as_string()
session.sendmail(YOUR_EMAIL, YOUR_DESTINATION_EMAIL, text)
session.quit
print('Mail is sent')


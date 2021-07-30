##########################################
# Adapted from FreeCodeCamp.org's "Python Networking Basics" by Neural Nine
# and realpython.com's "Sending Emails with Python" by Joska de Langen
##########################################

import smtplib, ssl
from email.mime.text import MIMEText            # format we will be using for displaying text
from email.mime.multipart import MIMEMultipart  # format we will be using to structure our email

PORT = 465                                      # default smtp-over-ssl port

context = ssl.create_default_context()          # import system certs

with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    
    # TODO encrypt local usr/pw storage
    
    with open("user.txt", "r") as f:            # read in username and pw
        username = f.readline()
        password = f.readline()

    server.login(username, password)

    msg = MIMEMultipart()                       # initialize new email
    msg['From'] = username                      # set email header contents
    msg['To'] = username
    msg['Subject'] = "Test Email for Python Networking Course"

    with open("body.txt", "r") as f:            # read in email body
        body = f.read()

    msg.attach(MIMEText(body, 'plain'))         # attach body to email
    text = msg.as_string()
    server.sendmail(username, username, text)
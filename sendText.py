#!/usr/bin/env python

def getCredentials():
    '''Get gmail login credentials'''

    import pickle

    with open('./PRIVATE/credentials','rb') as newCredentials:
        credentials = pickle.loads(newCredentials.read())

    return credentials

def sendText(subjectIn, message, credentials, recipient):
    '''Send a text containing a message'''
    
    import smtplib
    
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    
    sender = credentials['login']
    password = credentials['password']
    
    subject = str(subjectIn)
    body = "" + str(message) + ""
    
    headers = ["From: " + sender, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/plain"]
    
    headers = "\r\n".join(headers)
    
    session = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender,password)
    
    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    
    session.close()
    #session.quit()

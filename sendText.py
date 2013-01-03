#!/usr/bin/env python

def getCredentials():
    '''Get gmail login credentials
    Format:
    'login'    : 'USERNAME @ gmail.com',
    'password' : 'PASSWORD',
    'phone'    : 'PHONE NUMBER @ provider'
    '''

    import pickle

    with open('./PRIVATE/credentials','rb') as newCredentials:
        credentials = pickle.loads(newCredentials.read())

    return credentials

def getRecepients():
    '''Get recipients'''
    
    import pickle
    
    with open('./PRIVATE/recepients','rb') as newRecepients:
        recepients = pickle.loads(newRecepients.read())

    return recepients

def sendText(subjectIn, message, credentials, recipient):
    '''Send a text containing a message'''
    
    import smtplib
    
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    
    sender = credentials['login']
    password = credentials['password']
    
    subject = str(subjectIn)
    body = "" + str(message) + ""
    
    # here 'recipient' must be a STRING
    headers = ["From: " + sender, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/plain"]
    
    headers = "\r\n".join(headers)
    
    session = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender,password)
    
    # here 'recipient' must be a LIST
    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    
    session.close()
    #session.quit()

#!/usr/bin/env python

def sendText(message, credentials):
    '''Send a text containing a message'''
    
    import smtplib
    
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    
    sender = credentials['login']
    #recipient = credentials['phone']
    #test email
    recipient = "litwhistle@mailinator.com"
    password = credentials['password']
    subject = 'SIMULATED'
    
    from time import gmtime, strftime
    timeNow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    body = 'SIMULATED disaster drill at {}'.format(timeNow)
    
    body = "" + body + ""
    
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

def getCredentials():
    '''Get gmail login credentials'''

    import pickle

    with open('./PRIVATE/credentials','rb') as newCredentials:
        credentials = pickle.loads(newCredentials.read())

    return credentials

def main():
    
    sendText("hello",getCredentials())
    
if __name__ == '__main__':
    main()
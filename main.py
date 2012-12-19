#!/usr/bin/env python



def main():
    
    from sendText import sendText, getCredentials
    
    subject = 'SIMULATED'
    recipient = "litwhistle@mailinator.com"
    
    #recipient = getCredentials()['phone']
    
    from time import gmtime, strftime
    timeNow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    body = 'SIMULATED disaster drill at {}'.format(timeNow)
    
    #print (recipient)
    
    sendText(subject, body, getCredentials(), recipient)
    
if __name__ == '__main__':
    main()
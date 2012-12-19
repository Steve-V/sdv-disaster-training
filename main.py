#!/usr/bin/env python

import pickle

def sendText(message):
    '''Send a text containing a message'''
    
    #TODO: create network code here
    
    #placeholder
    print( "Simulated sending of: {}".format(message))
    
    return

def getCredentials():
    
    with open('./PRIVATE/credentials','rb') as newCredentials:
        credentials = pickle.loads(newCredentials.read())
    
    return credentials

def main():
    
    getCredentials()
    
if __name__ == '__main__':
    main()
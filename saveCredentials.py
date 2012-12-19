#!/usr/bin/env python

def saveCredentials():
    '''Save gmail login credentials'''
    
    #this function for reference only
    
    import pickle
    
    newData = {
        'login'    : 'USERNAME @ gmail.com',
        'password' : 'PASSWORD',
        'phone'    : 'PHONE NUMBER @ provider'
        # provider list here:
        # http://www.emailtextmessages.com/
        }
    
    with open('NEWcredentials','wb') as newFile:
        pickle.dump(newData,newFile)


if __name__ == '__main__':
    main()
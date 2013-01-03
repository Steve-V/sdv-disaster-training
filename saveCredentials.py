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

def saveCredentials():
    '''Save recepients'''
    
    #this function for reference only
    
    import pickle
    
    recepients = ("phone@provider","email@provider","phone@provider")
    
    with open('NEWrecepients','wb') as newFile:
        pickle.dump(recepients,newFile)


if __name__ == '__main__':
    main()
#!/usr/bin/env python

def getDisaster():
    import random
    
    disasters = (
        'small fire',
        'whole room on fire',
        'building on fire',
        'tornado warning',
        'zombie apocalypse',
        'single raptor attack',
        'multiple raptor attack',
        'local active shooter',
        'flood warning',
        'volcanic eruption',
        'distant explosion',
        'earthquake',
        'riot in progress',
        'unruly crowd approaching',
        'toxic gas release',
        'nerve gas release',
        'smell of natural gas',
        'unidentified loud noise',
        'radiation leak',
        'enemy air raid',
        'car bomb explosion',
        'car bomb threat',
        'pipe bomb threat',
        'mail bomb threat',
        'GA aircraft crash',
        'airliner crash',
        'train derail',
        'car-train collision',
        'head-on car accident',
        'T-bone car accident',
        'drunk driver spotted',
        'sniper at long range',
        'blizzard',
        'icy roads',
        'zero visibility',
        'nosebleed',
        'man hitting man',
        'man hitting woman',
        'woman hitting man',
        'group hitting man',
        'group hitting cop',
        'rape in progress, one rapist',
        'rape in progress, multiple rapists',
        'man bleeding without obvious cause'
        'police officer shot',
        'police foot chase',
        'police car chase',
        'woman screaming in distance',
        'loud shouts in distance',
        'loud bang, close by',
        'nauseating smell',
        'sudden vomiting',
        'being pursued on foot by individual',
        'being pursued on foot by group'
        'being pursued in vehicle by vehicle'
        )
    
    return random.choice(disasters)

def main():
    
    from sendText import sendText, getCredentials
    
    subject = 'SIMULATED'
    #recipient = "litwhistle@mailinator.com"
    
    recipient = getCredentials()['phone']
    
    from time import gmtime, strftime
    timeNow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    body = 'SIMULATED disaster drill at {}'.format(timeNow)
    
    #print (recipient)
    
    sendText(subject, body, getCredentials(), recipient)

def runDebug():
    print( getDisaster() )


if __name__ == '__main__':
    #main()
    runDebug()

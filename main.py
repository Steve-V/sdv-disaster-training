#!/usr/bin/env python

def getDisaster():
    import random
    
    disasters = (
        #natural
        {'description' : 'small fire'},
        {'description' : 'whole room on fire'},
        {'description' : 'building on fire'},
        {'description' : 'tornado warning'},
        {'description' : 'flood warning'},
        {'description' : 'volcanic eruption'},
        {'description' : 'earthquake'},
        {'description' : 'blizzard'},
        {'description' : 'icy roads'},
        {'description' : 'zero visibility'},
        
        ##silly
        #{'description' : 'zombie apocalypse'},
        #{'description' : 'single raptor attack'},
        #{'description' : 'multiple raptor attack'},
        
        #social / military / crime
        {'description' : 'riot in progress'},
        {'description' : 'unruly crowd approaching'},
        {'description' : 'enemy air raid'},
        {'description' : 'drunk driver spotted'},
        {'description' : 'two men fighting'},
        {'description' : 'two women fighting'},
        {'description' : 'child alone and crying'},
        {'description' : 'man beating man'},
        {'description' : 'man beating woman'},
        {'description' : 'woman beating man'},
        {'description' : 'group beating man'},
        {'description' : 'group beating cop'},
        {'description' : 'rape in progress nearby, one rapist'},
        {'description' : 'rape in progress nearby, multiple rapists'},
        {'description' : 'police officer shot'},
        {'description' : 'police foot chase'},
        {'description' : 'police car chase'},
        {'description' : 'being pursued on foot by individual'},
        {'description' : 'being pursued on foot by group'},
        {'description' : 'being pursued in vehicle by vehicle'},
        
        #terror
        {'description' : 'shooter in the area'},
        {'description' : 'car bomb explosion'},
        {'description' : 'car bomb threat'},
        {'description' : 'pipe bomb threat'},
        {'description' : 'mail bomb threat'},
        {'description' : 'car bomb discovered, detonation in 5 minutes'},
        {'description' : 'pipe bomb discovered, detonation in 5 minutes'},
        {'description' : 'mail bomb discovered, detonation in 5 minutes'},
        {'description' : 'incoming sniper fire from long range'},
        
        #mystery / misc
        {'description' : 'distant explosion'},
        {'description' : 'toxic gas release'},
        {'description' : 'nerve gas release'},
        {'description' : 'smell of natural gas'},
        {'description' : 'unidentified loud noise'},
        {'description' : 'radiation leak'},
        {'description' : 'woman screaming in distance'},
        {'description' : 'loud shouts in distance'},
        {'description' : 'loud bang, close by'},
        
        #accidents
        {'description' : 'small aircraft crash nearby'},
        {'description' : 'airliner crash nearby'},
        {'description' : 'train derailed nearby'},
        {'description' : 'car-train collision nearby'},
        {'description' : 'head-on car accident nearby'},
        {'description' : 'T-bone car accident nearby'},
        
        #medical
        {'description' : 'nosebleed'},
        {'description' : 'man bleeding without obvious cause'},
        {'description' : 'nauseating smell'},
        {'description' : 'sudden vomiting'},
        {'description' : 'person begins choking nearby'},
        {'description' : 'person unresponsive after falling, hitting head'}
        
        )
    
    return random.choice(disasters)['description']

def main():
    
    from sendText import sendText, getCredentials
    
    subject = 'SIMULATED Crisis'
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

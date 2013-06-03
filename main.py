#!/usr/bin/env python

def getDisaster():
    import random
    
    disasters = (
        #natural
        {'description' : 'Small fire'},
        {'description' : 'Whole room on fire'},
        {'description' : 'Building on fire'},
        {'description' : 'Tornado warning'},
        {'description' : 'Flood warning'},
        {'description' : 'Volcanic eruption'},
        {'description' : 'Earthquake'},
        {'description' : 'Blizzard'},
        {'description' : 'Icy roads'},
        {'description' : 'Zero visibility'},
        
        ##silly
        #{'description' : 'Zombie apocalypse'},
        #{'description' : 'Single raptor attack'},
        #{'description' : 'Multiple raptor attack'},
        
        #social / military / crime
        {'description' : 'Riot in progress'},
        {'description' : 'Unruly crowd approaching'},
        {'description' : 'Enemy air raid'},
        {'description' : 'Drunk driver spotted'},
        {'description' : 'Two men fighting'},
        {'description' : 'Two women fighting'},
        {'description' : 'Child alone and crying'},
        {'description' : 'Man beating man'},
        {'description' : 'Man beating woman'},
        {'description' : 'Woman beating man'},
        {'description' : 'Group beating man'},
        {'description' : 'Group beating cop'},
        {'description' : 'Rape in progress nearby, one rapist'},
        {'description' : 'Rape in progress nearby, multiple rapists'},
        {'description' : 'Police officer shot'},
        {'description' : 'Police foot chase'},
        {'description' : 'Police car chase'},
        {'description' : 'Being pursued on foot by individual'},
        {'description' : 'Being pursued on foot by group'},
        {'description' : 'Being pursued in vehicle by vehicle'},
        
        #terror
        {'description' : 'Shooter in the area'},
        {'description' : 'Car bomb explosion'},
        {'description' : 'Car bomb threat'},
        {'description' : 'Pipe bomb threat'},
        {'description' : 'Mail bomb threat'},
        {'description' : 'Car bomb discovered, detonation in 5 minutes'},
        {'description' : 'Pipe bomb discovered, detonation in 5 minutes'},
        {'description' : 'Mail bomb discovered, detonation in 5 minutes'},
        {'description' : 'Incoming sniper fire from long range'},
        
        #mystery / misc
        {'description' : 'Distant explosion'},
        {'description' : 'Toxic gas release'},
        {'description' : 'Nerve gas release'},
        {'description' : 'Strong smell of natural gas'},
        {'description' : 'Unidentified loud noise'},
        {'description' : 'Radiation leak'},
        {'description' : 'Woman screaming in distance'},
        {'description' : 'Loud shouts in distance'},
        {'description' : 'Loud bang, close by'},
        
        #accidents
        {'description' : 'Small aircraft crash nearby'},
        {'description' : 'Airliner crash nearby'},
        {'description' : 'Train derailed nearby'},
        {'description' : 'Car-train collision nearby'},
        {'description' : 'Head-on car accident nearby'},
        {'description' : 'T-bone car accident nearby'},
        
        #medical
        {'description' : 'Nosebleed'},
        {'description' : 'Man bleeding without obvious cause'},
        {'description' : 'Nauseating smell'},
        {'description' : 'Sudden vomiting'},
        {'description' : 'Person begins choking nearby'},
        {'description' : 'Person unresponsive after falling, hitting head'}
        
        )
    
    return random.choice(disasters)['description']

def getStatus():
    '''Returns various status effects'''
    
    import random
    
    # Chances (out of 100)
    armedChance = 50
    hurtChance = 20
    aloneChance = 60
    groupChance = 40
    
    isArmed = "Armed, " if (random.randint(1,100) < armedChance) else "Unarmed, "
    
    isHurt = "injured, " if (random.randint(1,100) < hurtChance) else ""
    
    #must determine this first, might or might not be used
    isGroup = "with group." if (random.randint(1,100) < groupChance) else "with friend."
    
    isAlone = "alone." if (random.randint(1,100) < aloneChance) else isGroup
    
    body = isArmed + isHurt + isAlone
    
    #print(body)
    
    return(body)
    
def disaster():
    from sendText import sendText, getCredentials, getRecepients
    
    subject = 'SIMULATED Alert'
    
    recepients = getRecepients()
    
    #recepients = ('litwhistle@mailinator.com')
    
    body = 'SIMULATED alert. Situation: {}. Your status: {}'.format( getDisaster(), getStatus() )
    
    print (body)
    
    #print (recepients[0])
    
    sendText(subject,body,getCredentials(),recepients[0])
    
    #for eachRecepient in recepients:
        #print (eachRecepient)
        #sendText(subject, body, getCredentials(), eachRecepient)

def exits():
    from sendText import sendText, getCredentials, getRecepients
    
    subject = 'Exits'
    
    recepients = getRecepients()
    
    #recepients = ('litwhistle@mailinator.com')
    
    body = 'Reminder: Nearest Exit?'
    
    print (body)
    
    #print (recepients[0])
    
    sendText(subject,body,getCredentials(),recepients[0])

def runDebug():
    from sendText import getRecepients
    print( getRecepients() )
    print( getRecepients()[0] )

def main():
    
    import random
    if random.randint(1,4000) < 10:
        if random.randint(1,100) < 80:
            exits()
        else:
            disaster()
    else:
        print("You got lucky this time")

if __name__ == '__main__':
    main()
    #runDebug()

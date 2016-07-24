import database


#For incrementing self-destruct counter
def incrementSD(doc):
    
    sdCounter=''
    
    if doc['sdCounter'] != '':

        sdCounter = int(doc['sdCounter'])
        sdCounter -= 1
    
        if sdCounter < 1:
         database.deleteDBEntry(doc)
        else: 
            doc['sdCounter'] = unicode(sdCounter)
            database.updateDBEntry(doc)
            
    return sdCounter
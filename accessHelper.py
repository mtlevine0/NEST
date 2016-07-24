import database


#For incrementing self-destruct counter
def incrementSD(doc):
    
    sdCounter = int(doc['self_destruct_count'])
    sdCounter -= 1
    
    if sdCounter == 0:
        database.deleteDBEntry(doc)
    else: 
        doc['self_destruct_count'] = unicode(sdCounter)
        database.updateDBEntry(doc)
            
    return sdCounter
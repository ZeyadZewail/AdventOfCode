
Guide = {'Rock':'Paper','Paper':'Scissors','Scissors':'Rock'}

def decide(p1,p2):
    
    if(p1 == p2):
        print('Draw')
        return

    if(p2 == Guide[p1]):
        print('Win')
        return 
    else:
        print('Lose')
        return


decide('Rock','Paper')
decide('Paper','Paper')
decide('Rock','Rock')
decide('Paper','Rock')
decide('Scissors','Rock')
decide('Rock','Scissors')
    
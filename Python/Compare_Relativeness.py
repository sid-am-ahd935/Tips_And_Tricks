


def checkCloseness(x, y):
    result = x/((x+y)/2)  * 100
    # 0   : x is far less than y
    # 200 : x is far greater than y
    # 100 : x == y
    return result

def checkPercent(x, y):
    result = checkCloseness(x, y)
    difference = 100 - abs(100-result)   
    # 0   : x==y;  
    # 100 : x far away from y
    return difference
    

def convertRange(OldValue, OldMin= -(__import__('sys').maxsize), OldMax= __import__('sys').maxsize, NewMin= 0, NewMax= 100):
    NewValue = ((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin) + NewMin
    # Old Range by default is -2**63 to 2**63
    # New Range by default is 0 to 100
    return NewValue


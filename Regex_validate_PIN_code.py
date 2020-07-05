def validate_pin(pin):
    #return true or false
    
    if len(pin)==4 or len(pin)==6:
        if pin.isdigit() == True:
            return True
        else:             #if pin.isdigit()== False then it should return false
            return False
    else:
        return False
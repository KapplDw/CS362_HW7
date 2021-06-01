## Dwight Kappl

def whole_Number(x):
    # Means Whole number
    if (x - int(x) == 0):
        return True
    else:
        return False


def leap(year):
    # Main code
    
        # Converts string year to an int
    year = int(year)
        # Checks if divisible by 4
    temp = year / 4.0
    if not whole_Number(temp):
        return False
        # Checks if divisible by 100
    temp = year / 100.0
    if not whole_Number(temp):
        return True
            
        # Checks if divisible by 400
    temp = year / 400.0
    if not whole_Number(temp):
        return False
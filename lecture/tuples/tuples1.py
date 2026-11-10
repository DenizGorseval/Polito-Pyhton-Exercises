# Function definition
def readDate() :
    print("Enter a date:")
    month = int(input(" month: "))
    day = int(input(" day: "))
    year = int(input(" year: "))
    return (year, month, day) # Returns a tuple.
    
    # Function call: assign entire value to a tuple
date = readDate()
    # Function call: use tuple assignment:
print(date)
def lineargrade(p): #takes the point value recieved and calculates grade in scale of 1.0, 1.5...6.0
    if p <= 12:
        return 6.0
    elif p > 12 and p < 57:
        return .5 * round(((-5 / 45) * (p - 57) + 1) / .5)

def passed(p): #takes in point value and returns True if grade is passing(<=4.0)
    if lineargrade(p) <= 4.0:
        return True
    else:
        return False
passed(0)

def mark(grade): #takes grade value and assigns it a letter grade
    if grade >= 6.0:
        print("F")
    elif grade  >= 5.0:
        print("E")
    elif grade >= 4.0:
        print("D")
    elif grade >= 3.0:
        print("C")
    elif grade >= 2.0:
        print("B")
    else:
        print("A")
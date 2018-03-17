def passq(score):
    if score>100:
        return("Invalid Entry")
    elif score>=90:
        return("A")
    elif score>=80:
        return("B")
    elif score>=70:
        return("C")
    elif score>=60:
        return("D")
    elif score>=0:
        return("Failed")
    else:
        return("Invalid Entry")
print(passq(71))

#Jake Hayes - 09/21/2016 

#Case 1 & 2 - Number Wizard
def nogerof():
    tot = 0 #total sum
    for i in range(1, 4):
        printQuestion(i)
        temp = input()
        tot += temp
    if(tot % 2 == 0):
        print('That is an even number.')
    else:
        print('That is an odd number.')
    return

def printQuestion(n): #Can print question up to the fifth
    try:
        tense = ['first ', 'second', 'third ', 'fourth', 'fifth ']
        print('Now tell me your ' + tense[n-1] + ' number: '),
    except IndexError:
        print("Error! Only capable for numbers 1-5.")
    return
 


#Case 3 - Common Characters
def commonChars(str1, str2):
    comChars = []
    for i in str1:
        for j in str2:
            if i == j and i not in comChars:
                comChars.append(i)
    print(comChars)
    return

str1 = "qwertyuiop "
str2 = "A quick brown fox jumps over the lazy dog"

#Question 1 - get sum, average, and standard deviation all together
def get_sum_avg_std(num = []):
    tot = 0
    length = len(num)
    for i in num:
        tot += i
    avg = tot / length
    stdDev = 0
    for j in num:
        stdDev += (j - avg)**2
    stdDev = stdDev / length
    stdDev = stdDev**0.5
    retTuple = tot, avg, stdDev
    return retTuple

num = [1, -123, 2, 4, 5, 10, 20, 30, 40, 50, 100, 4, 3, 2, 1, 4, 3, 2, 1]

#nogerof()
#commonChars(str1, str2)
#print(get_sum_avg_std(num))

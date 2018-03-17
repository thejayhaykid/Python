from random import *
#L04-1
def showASCII(s1):
    for i in range(len(s1)):
        print(s1[i],"=",ord(s1[i]))
##showASCII("ABCD")
#L04-2
def printASCIIRange(n1,n2):
    if n2>n1:
        length=n2-n1
        counter=1
    else:
        length=n1-n2
        counter=0
    for i in range(length+1):
        if counter==1:
            print(n1,"=",chr(n1))
            n1=n1+1
        else:
            print(n1,"=",chr(n2))
            n2=n2+1
##printASCIIRange(65,69)
#L04-3
def reverseString(message):
    r1=len(message)
    reverse=""
    for i in range(len(message)):
##        print(i)
        reverse=reverse+message[r1-1]
        r1=r1-1
    return reverse
##print(reverseString("Hello"))
def reverseString2(message):
    print(message[::-1])
##reverseString2("Hello")
def reverseString3(message):
    reverse=""
    for i in range(len(message)):
        reverse=message[i-len(message)]+reverse
    return reverse
##print(reverseString3("Hello"))
#L04-4
def changeCase(letter):
    test=ord(letter)
    if test>=65 and test<=90:
        test=test+32
        answer=chr(test)
    elif test>=97 and test<=122:
        test=test-32
        answer=chr(test)
    else:
        answer="INVALID INPUT"
    return(answer)
##print(changeCase("a"))
#L04-5
def lowerCase(message):
    finalMessage=""
    for i in range(len(message)):
        test=ord(message[i])
        if test>=65 and test<=90:
            test=ord(changeCase(chr(test)))
        finalMessage=finalMessage+chr(test)
    return finalMessage
##print(lowerCase("123 HeLlo BOB #$% abcD"))
#L04-6
def formatLongDate(date):
    month=date[:2]
    day=date[3:5]
    year=date[6:]
##    print(month,day,year)
    if month=="01":
        month1="January"
    elif month=="02":
        month1="February"
    elif month=="03":
        month1="March"
    elif month=="04":
        month1="April"
    elif month=="05":
        month1="May"
    elif month=="06":
        month1="June"
    elif month=="07":
        month1="July"
    elif month=="08":
        month1="August"
    elif month=="09":
        month1="September"
    elif month=="10":
        month1="October"
    elif month=="11":
        month1="November"
    elif month=="12":
        month1="December"
    else:
        month1="INVALID INPUT"
    print(month1,day,", 20",year)
##formatLongDate("09/05/99")
#L04-7
def ASCIICodesToString(code):
    length=len(code)//3
    l1=0
    l2=3
    message=""
    for i in range(length):
        code1=int(code[l1:l2])
        message=message+chr(code1)
        l1=l1+3
        l2=l2+3
    return message
##print(ASCIICodesToString("066065068"))
#L04-8
def stringToAsciiCodes(string):
    code=""
    for i in range(len(string)):
        if ord(string[i])<100:
            code=code+"0"
        code=code+str(ord(string[i]))
    return code
##print(stringToAsciiCodes("BAD"))
#L04-9
def encryptTranspose(message):
    evenChars = ""    
    oddChars = ""    
    for i in range (len(message)):
        if i % 2 == 0:                          
            evenChars = evenChars + message[i]
        else:            
            oddChars = oddChars + message[i]
    cipherText = oddChars + evenChars    
    return cipherText
##print(encryptTranspose("Jake Hayes"))
def encryptTranspose2(message):
    firstChars=""
    secondChars=""
    thirdChars=""
    fourthChars=""
    for i in range(len(message)):
        if i%4==0:
            fourthChars=fourthChars+message[i]
        elif (i-1)%4==0:
            thirdChars=thirdChars+message[i]
        elif i%2==0:
            secondChars=secondChars+message[i]
        else:
            firstChars=firstChars+message[i]
    encryptText=firstChars+secondChars+thirdChars+fourthChars
    if (len(secondChars)<len(firstChars)):
        encryptText=encryptText+firstChars[-1]
    elif len(thirdChars)<len(secondChars):
        encryptText=encryptText+fistChars[-1]+secondChars[-1]
    elif len(fourthChars)<len(thirdChars):
        encryptText=encryptText+fistChars[-1]+secondChars[-1]+thirdChars[-1]
    return encryptText
##print(encryptTranspose2("Jake Hayes"))
def encryptSubstitute(message):
    key = "zxcvbnmasdfghjklqwertyuiop "
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    message = message.lower()
    cipherText = ""
    for ch in message:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText
##print(encryptSubstitute("Jake Hayes"))
#L04-10
def PRS(p1,p2):
  if p1=="rock" and p2=="scissors":
    print("rock dulls scissors, p1 wins")
    return 1
  elif p1=="scissors" and p2=="paper":
    print("scissors cuts paper, p1 wins")
    return 1
  elif p1=="paper" and p2=="rock":
    print("paper covers rock, p1 wins")
    return 1
  elif p2=="rock" and p1=="scissors":
    print("rock dulls scissors, p2 wins")
    return 2
  elif p2=="scissors" and p1=="paper":
    print("scissors cuts paper, p2 wins")
    return 2
  elif p2=="paper" and p1=="rock":
    print("paper covers rock, p2 wins")
    return 2
  elif p1==p2:
    print("TIE!")
    return 3
  else:
    print("Invalid Entry")
    return 0
def PRSTournament():
    counterP1=0
    counterP2=0
    tieCounter=0
    for i in range(10):
        p1=randint(1,3)
        p2=randint(1,3)
        if p1==1:
            pl1="rock"
        elif p1==2:
            pl1="paper"
        else:
            pl1="scissors"
        if p2==1:
            pl2="rock"
        elif p2==2:
            pl2="paper"
        else:
            pl2="scissors"
        score=PRS(pl1,pl2)
        if score==1:
            counterP1=counterP1+1
            print("Player 1 wins! Player 1 has",counterP1,"wins and Player 2 has",counterP2,"wins.")
        elif score==2:
            counterP2=counterP2+1
            print("Player 2 wins! Player 2 has",counterP2,"wins and Player 1 has",counterP1,"wins.")
        elif score==3:
            tieCounter=tieCounter+1
            print("TIE! The score is",counterP1,"to",counterP2)
        if counterP1>=3:
            print("PLAYER 1 WINS!! Player 1 wins with a final score of",counterP1,"to",counterP2)
            return "P1"
        elif counterP2>=3:
            print("PLAYER 2 WINS!! Player 2 wins with a final score of",counterP2,"to",counterP1)
            return "P2"
        elif tieCounter>=3:
            print("TIE! There have been",tieCounter,"ties.")
            return "TIE"
PRSTournament()        

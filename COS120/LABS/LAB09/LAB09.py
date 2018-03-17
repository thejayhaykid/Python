###L09-01
def rainRightJust():
    rainfile = open("rainfall.txt","r")
    outfile = open("rainfallRightJust.txt","w")

    for aLine in rainfile:
        values = aLine.split()
        cityNames=values[0]
        numbers=values[1]
        outfile.write("%+25s %+5s \n" % (cityNames,numbers))

    rainfile.close()
    outfile.close()
##rainRightJust()
###L09-02
def fahrToCels():
    outfile = open("tempconv.txt","w")

    fahr="Fahrenheit"
    cels="Celsius"
    outfile.write("%+10s %+10s \n" % (fahr,cels))

    for fahrTemp in range(-300,212,1):
        celsTemp=(fahrTemp-32)*(5/9)
        outfile.write("%10.3f %10.3f \n" % (fahrTemp,celsTemp))

    outfile.close()
##fahrToCels()
###L09-03
def readLines():
    rainfile=open("rainfall.txt","r")
    print(rainfile.readline())
    print(rainfile.readline())
    print(rainfile.readlines())
    rainfile.close()
##readLines()
###L09-04
def readLines2():
    rainfile=open("rainfall.txt","r")
    print(rainfile.readlines())
    rainfile.close()
##readLines2()
###L09-05
def PsalmUpper():
    psalm=open("psalm112.txt","r")
    PSALM=open("psalm112Upper.txt","w")
    for aLine in psalm:
        psalmRead=psalm.readlines()
        PSALM.write(str([x.upper() for x in psalmRead]))
    psalm.close()
    PSALM.close()
##PsalmUpper()
###L09-06
def counting():
    psalm=open("psalm112.txt","r")
    lines=0
    words=0
    characters=0
    for aLine in psalm:
        lines+=1
        words1=aLine.split()
        for aWord in words1:
            words+=1
            for aChar in aWord:
                characters+=1
            characters+=1
    print(lines," lines")
    print(words," words")
    print(characters," characters")
    psalm.close()
##counting()
###L09-07
def concord():
    textIn=open("textIn.txt","r")
    concord=open("concord.txt","w")
    D={}
    linecount=0
    for aLine in textIn:
        linecount+=1
        words=aLine.split()
        for word in words:
            if word in D:
                D[word].append(linecount)
            else:
                D[word]=[linecount]
    for keys in D:
        concord.write("%+15s %s \n" % (keys,str(D[keys])))
    textIn.close()
    concord.close()

##concord()
###L09-08
def readStudentScores(fileName,pointsD,scoresD):
    studentScores=open(fileName,"w")
    keys=list(pointsD)
    keys.sort()
    for key in keys:
        studentScores.write("%+3s %s" % (key,str(pointsD[key])))
    studentScores.write("\n")
    for key in scoresD:
        studentScores.write("%s" % (key))
        scores=list(scoresD[key])
        scores.sort()
        for score in scores:
            studentScores.write("%+3s %i" % (score,scoresD[key][score]))
        studentScores.write("\n")
    studentScores.close()


PPD={'T1':100, 'T2':100, 'H1':10, 'H2':20}
SSD={'Jones':{'T1':100, 'T2':100, 'H1':10, 'H2':20},'Smith':{'T1':95, 'T2':100, 'H1':10, 'H2':12}, 'Armes': {'T1':100, 'T2':95, 'H1':0, 'H2':18}}
readStudentScores("students_scores.txt",PPD,SSD)
###L09-09
def printScoresMatrix(scoresD):
    studentScores=open("scoresMatrix.txt","w")
    keys=['T1', 'T2', 'H1', 'H2']
    keys.sort()
    studentScores.write("     ")
    for key in keys:
        studentScores.write("%+5s" % (key))
        space=5
    studentScores.write("\n")
    for key in scoresD:
        studentScores.write("%s" % (key))
        scores=list(scoresD[key])
        scores.sort()
        for score in scores:
            studentScores.write("%5i" % (scoresD[key][score]))
        studentScores.write("\n")
    studentScores.close()

printScoresMatrix(SSD)
###L09-10
def printScoresMatrix1(scoresD):
    studentScores=open("scoresMatrixAverage.txt","w")
    keys=['T1', 'T2', 'H1', 'H2']
    keys.sort()
    studentScores.write("     ")
    H1=0
    H2=0
    T1=0
    T2=0
    for key in keys:
        studentScores.write("%+5s" % (key))
        space=5
    studentScores.write("\n")
    student1=0
    student2=0
    student3=0
    for key in scoresD:
        studentScores.write("%s" % (key))
        scores=list(scoresD[key])
        scores.sort()
        counter=1
        for score in scores:
            studentScores.write("%5i" % (scoresD[key][score]))
##            print(scoresD[key],scoresD[key][score])
            if score=='H1':
                H1=H1+scoresD[key][score]
##                print(H1)
            elif score=='H2':
                H2=H2+scoresD[key][score]
##                print(H2)
            elif score=='T2':
                T2=T2+scoresD[key][score]
##                print(T2)
            elif score=='T1':
                T1=T1+scoresD[key][score]
##                print(T1)
            student1=student1+(scoresD[key][score])
        student1=student1/4
        studentScores.write("%5.1f" % (student1))
        studentScores.write("\n")
    H1A=H1/3
    H2A=H2/3
    T1A=T1/3
    T2A=T2/3
##    print(H1,H2,T1,T2,H1A,H2A,T1A,T2A)
    studentScores.write("     ")
    studentScores.write("%5.1f %5.1f %5.1f %5.1f" % (H1A,H2A,T1A,T2A))
    studentScores.close()
    

printScoresMatrix1(SSD)

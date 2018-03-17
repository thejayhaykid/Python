def readGradesStructures(fileName,assignD,studentsD):
    inFile=open(fileName,"r")
    firstLine=inFile.readline()
    firstLineList=firstLine.split()
    for i in range(0,len(firstLineList)-1,2):
        assignD[firstLineList[i]]=int(firstLineList[i+1])
    for eachLine in inFile:
        stuScoresList=eachLine.split()
        name=stuScoresList.pop(0)
        scores={}
        for i in range(0,len(stuScoresList)-1,2):
            scores[stuScoresList[i]]=int(stuScoresList[i+1])
        studentsD[name]=scores
    inFile.close()

def writeGradesStructures(fileName,assignD,studentsD):
    outFile=open(fileName,"w")
    for aKey in assignD:
        outFile.write(aKey + " " + str(assignD[aKey]) + " ")
    outFile.write("\n")
    for sKey in studentsD:
        outFile.write(sKey + " ")
        for aKey in studentsD[sKey]:
            outFile.write(aKey + " " + str(studentsD[sKey][aKey]) + " ")
        outFile.write("\n")
    outFile.close()    

def printScoresMatrix(assignD,studentsD):
    assignList=list(assignD.keys())
    assignList.sort()
    studentList=list(studentsD.keys())
    studentList.sort()
    print("%+14s" % assignList[0],end="")
    for index in range(1,len(assignList)):
        print("%+4s" % assignList[index], end="")
    print()
    for student in studentList:
        print("%+10s" % student,end="")
        for assignNameKey in assignList:
            print("%4d" % studentsD[student][assignNameKey],end="")
        print()
    print()
    
def addAStudent(assignD,studentsD):
##    print("In addAStudent")
    name=input("Enter the student name => ")
    while name in studentsD:
        print("Name",name,"already exists!")
        name=input("Enter the student name => ")
    scores={}
    for eachAssignKey in assignD:
        score=int(input("Enter a score for "+name+" for "+eachAssignKey+"=> "))
        while score > assignD[eachAssignKey]:
            print("Score exceeds maximum of",assignD[eachAssignKey])
            score=int(input("Enter a score for "+name+" for "+eachAssignKey+"=> "))
        scores[eachAssignKey]=score
    studentsD[name]=scores

def addAnAssignment(assignD,studentsD):
##    print("In addAnAssignment")
    name=input("Enter the new assignment name => ")
    while name in assignD:
        print("That assignment already exists!")
        name=input("Enter the new assignment name => ")
    score=int(input("Enter the maximum score for this assignment => "))
    assignD[name]=score
    for eachStudent in studentsD:
        studentScore=int(input("Enter "+eachStudent+"'s score on "+name+" => "))
        while studentScore > assignD[name]:
            print("Score exceeds maximum of",assignD[name])
            studentScore=int(input("Enter "+eachStudent+"'s score on "+name+" => "))
        studentsD[eachStudent][name]=studentScore

def updateAssignmentsForStudent(assignD,studentsD):
    student=input("Enter which student's scores you would like to update => ")
    while student not in studentsD:
        print("Student not in dictionary! Try again.")
        student=input("Enter which student's scores you would like to update => ")
    for eachAssignment in studentsD[student]:
        newScore=int(input("Enter the new score for "+student+" on "+eachAssignment+" => "))
        while newScore > assignD[eachAssignment]:
            print("Score too high!")
            newScore=int(input("Enter the new score for "+student+" on "+eachAssignment+" => "))
        studentsD[student][eachAssignment]=newScore

def updateAssignmentForStudents(assignD,studentsD):
    Assignment=input("Enter which assignment you would like to update => ")
    while Assignment not in assignD:
        print("Invalid assignment!")
        Assignment=input("Enter which assignment you would like to update => ")
    for eachStudent in studentsD:
        newScore=int(input("Enter the new score on "+Assignment+" for "+eachStudent+" => "))
        while newScore>assignD[Assignment]:
            print("Score too high!")
            newScore=int(input("Enter the new score on "+Assignment+" for "+eachStudent+" => "))
        studentsD[eachStudent][Assignment]=newScore

def updateAssignmentForStudent(assignD,studentsD):
    student=input("Enter which student you would like to update => ")
    while student not in studentsD:
        print(student,"not in dictionary.")
        student=input("Enter which student you would like to update => ")
    assignment=input("Enter which assignment you would like to update => ")
    while assignment not in assignD:
        print(assignment,"not in dictionary.")
        assignment=input("Enter which assignment you would like to update => ")
    score=int(input("Enter new score for "+student+" on "+assignment+" => "))
    while score>assignD[assignment]:
        print("Score too high!")
        score=int(input("Enter new score for "+student+" on "+assignment+" => "))
    studentsD[student][assignment]=score

def gradeReturn(grade):
    if grade>.9:
        return "A"
    elif grade > .8:
        return "B"
    elif grade > .7:
        return "C"
    elif grade > .6:
        return "D"
    else:
        return "F"

def printGradeReport(assignD,studentsD):
    assignList=list(assignD.keys())
    assignList.sort()
    studentList=list(studentsD.keys())
    studentList.sort()
    letterGrades=[]
    percentageList=[]
    overallPercentage=[]
    counter=0
    initial=0
    average=0
    length=len(assignList)
    for eachStudent in studentList:
        for eachScore in assignList:
            percentage=((studentsD[eachStudent][eachScore])/(assignD[eachScore]))
            percentageList.append(percentage)
            percentage=0
        for eachPerctentage in percentageList:
            initial=initial+eachPerctentage
        percentageList=[]
        average=0
        percentage=[]
        average=initial/length
        initial=0
        letterGrade=gradeReturn(average)
        average=average*100
        overallPercentage.append(average)
        average=0
        initial=0
        letterGrades.append(letterGrade)
    for student in studentList:
        print("%+10s" % student,end="")
        print("%4i %+2s" % (overallPercentage[counter],letterGrades[counter]),end="")
        counter=counter+1
        print()

def main():
    assignD={}
    studentsD={}
    readGradesStructures("student_scores.txt", assignD, studentsD)
    choice=0
    while choice!='8':
        print()
        print("1. Add a student")
        print("2. Add an assignment")
        print("3. Update all assignments for students")
        print("4. Update an assignment for all students")
        print("5. Update an assignment for a student")
        print("6. Display grade matrix")
        print("7. Print grade report")
        print("8. Exit")
        choice = input("Please select a menu item => ")
        print("")
        if choice=="1":
            addAStudent(assignD,studentsD)
        elif choice=="2":
            addAnAssignment(assignD,studentsD)
        elif choice=="3":
            updateAssignmentsForStudent(assignD,studentsD)
        elif choice=="4":
            updateAssignmentForStudents(assignD,studentsD)
        elif choice=="5":
            updateAssignmentForStudent(assignD,studentsD)
        elif choice=="6":
            printScoresMatrix(assignD,studentsD)
        elif choice=="7":
            printGradeReport(assignD,studentsD)
        elif choice=="8":
            writeGradesStructures("student_scores.txt",assignD,studentsD)
            print("File saved")
        else:
            print("INVALID MENU CHOICE!")

main()

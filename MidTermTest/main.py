import sys
from datetime import datetime

def openFile(fileName,mode):
    """Open and return an open file with the given permissions """
    try:
        file = open("Assets\\TestFiles\\"+fileName,mode)
    except IOError as e:
        print("Unable to open the file", fileName, "Ending program.\n", e)
        try:
            file = open("Assets\\Errors\\errorLog.txt","a+")
            time = datetime.now()
            errorTime = time.strftime("%m/%d/%Y %H:%M:%S")
            file.writelines(str(e)+" "+str(errorTime)+"\n")
            input("\n\nPress the enter key to exit.")
            sys.exit()
        except:
            sys.exit()

    else:
        return file

def nextLine(file):
    try:
        line = file.readline()
        line = line.replace("/","\n")
        return line
    except:
        print("Could not read line")
        sys.exit()

def nextQuestion(file):
    """Return the next question block of data from the trivia file."""
    category = nextLine(file)
    question = nextLine(file)
    answers = []
    for i in range(4):
        answers.append(nextLine(file))
    correct = nextLine(file)
    if correct:
        correct = correct[0]
    explanation = nextLine(file)

    return category,question,answers,correct,explanation

def getName():
    try:
        time = datetime.now()
        testTime = time.strftime("%m/%d %H:%M")
        while True:
            name = input("Please enter your name.")
            if len(name) >+ 3 and " " in name:
                name = name.title()
                return name, testTime
    except:
        print("GETNAMEFAILURE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def welcome(title,name,testTime):
    """Welcome the player"""
    print("Welcome "+name+" to your Mid Term Test\n")
    print("Your tester is "+title)

def createReportCard(name,score,totalQuestions):
    card = open("Assets\\ReportCards\\"+name+".txt","w")
    card.write("Name = "+name+"\n")
    card.write("Number Correct = "+str(score)+"\n")
    percentage = score/totalQuestions*100
    card.write("Percentage Correct = "+"%"+str(percentage)+"\n")
    if percentage >= 90:
        card.write("Letter Grade = A")
    elif percentage >= 80 and percentage < 90:
        card.write("Letter Grade = B")
    elif percentage >= 70 and percentage < 80:
        card.write("Letter Grade = C")
    elif percentage >= 60 and percentage < 70:
        card.write("Letter Grade = D")
    elif percentage < 60:
        card.write("Letter Grade = F")
    card.close()


def main():
    file = openFile("exampleTest.txt","r")#Will need to change file name to match the test you are taking.
    title = nextLine(file)
    name, testTime = getName()
    welcome(title,name,testTime)
    score = 0
    totalQuestions = 0
    category,question,answers,correct,explanation = nextQuestion(file)
    while category:
        totalQuestions += 1
        print(category)
        print(question)
        for i in range(len(answers)):
            print(str.format("\t{}:    {}",i+1,answers[i]))
        #get answer
        answer = input("What is your answer?")
        if answer == correct:
            print("\nRight!",end=" ")
            score+=1
        else:
            print("\nWrong.",end=" ")
        print(explanation)
        print("Score:",score,"\n\n")
        #get next block
        category,question,answers,correct,explanation = nextQuestion(file)
    file.close()
    print("That was the last question!")
    print("Your final score is",score)
    createReportCard(name,score,totalQuestions)




main()

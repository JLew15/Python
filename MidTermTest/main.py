import sys

def openFile(fileName,mode):
    """Open and return an open file with the given permissions """
    try:
        file = open("Assets\\TestFiles\\"+fileName,mode)
    except IOError as e:
        print("Unable to open the file", fileName, "Ending program.\n", e)
        try:
            file = open("Assets\\Errors\\errorLog.txt","a+")
            file.writelines(str(e))
            input("\n\nPress the enter key to exit.")
            sys.exit()
        except:
            sys.exit()

    else:
        return file



def main():
    file = openFile("exampleTest.txt","r")



main()

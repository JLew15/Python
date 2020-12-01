#Read it
#Jaiden Lewis
# 12/1/2020


#main
#textFile = open("Location","Permissions")
#try:
textFile = open("Assets\\SaveData\\random.txt","r")
#except:
    #print("That file did not exist.")
    #textFile = open("Assets\\SaveData\\testers.txt","w+")

lines = textFile.readlines()
print(lines)
for line in lines:
    print(line)

textFile.close()

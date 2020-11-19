def change_Rations(rations):
    print ("your current Rations are", rations)
    options = ["full","half","quarter"]
    index = 1
    for option in options:
        print(str.format("{}     {}",index,option))
        index+=1
    while True:
        try:
            choice = int(input("choose your pace"))
            if choice == 1:
                return "full"
            elif choice == 2:
                return "half"
            elif choice == 3:
                return "quarter"
            else:
                print("not an option")
        except:
            print ("not a good input")

def change_pace(pace):
    print ("your current pace is", pace)
    options = ["slow","normal","fast"]
    index = 1
    for option in options:
        print(str.format("{}     {}",index,option))
        index+=1
    while True:
        try:
            choice = int(input("choose your pace"))
            if choice == 1:
                return "slow"
            elif choice == 2:
                return "normal"
            elif choice == 3:
                return "fast"
            else:
                print("not an option")
        except:
            print ("not a good input")
rations = "full"
pace = "normal"
pace = change_pace(pace)
rations = change_Rations(rations)
print(pace)
print (rations)

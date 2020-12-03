import pickle, shelve

variety = ["hot","dill","sweet","bread and butter"]
shapes = ["relish","whole","sliced","chips","wavy"]
brand = ["claussen","heinz","vlassic","great value","western family"]

shelf = shelve.open("pickles2.dat")
shelf["variety"] = variety
shelf["shapes"] = shapes
shelf["brand"] = brand
shelf.sync()

print("brand",shelf["brand"])
print("shapes", shelf["shapes"])
print("variety", shelf["variety"])

shelf.close()

# file = open("Assets\\SaveData\\pickles1.dat","wb")
# pickle.dump(variety,file)
# pickle.dump(shapes,file)
# pickle.dump(brand,file)
# file.close()


# file = open("Assets\\SaveData\\pickles1.dat","rb")
# list1 = pickle.load(file)
# list2 = pickle.load(file)
# list3 = pickle.load(file)
# print(list1)
#
# print(list2)

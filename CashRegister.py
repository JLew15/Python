#Cash Register Assignment
#Jaiden Lewis

numItems = 4
costPerItem = 10.00
taxRate = 0.08
subTotal = numItems * costPerItem
taxAmount = subTotal * taxRate
totalPrice = subTotal + taxAmount

print("Number of items : " + str(numItems))
print("Cost per item   : $" + str(costPerItem))
print("Tax Rate...     : %" + str(taxRate * 100))
print("Tax amount      : $" + str(taxAmount))
print("TOTAL PRICE     : $" + str(totalPrice))

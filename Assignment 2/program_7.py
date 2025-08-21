a = int(input("Enter the Buying price: "))
b = int(input("Enter the selling price: "))
if (a-b) > 0:
    print("We got a loss and the loss is",a-b)
elif (a-b) <0:
    print("We got a profit and the profit is",b-a)
else :
    print("We neither got a profit nor loss")
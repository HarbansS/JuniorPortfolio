ans = input("did you order delivery?")
if ans == "yes":
    print("Great!")
    price = float(input("How much did the food cost"))
    people = int(input("How many people are eating from the order?"))
    print("Each person will have to pay $" + str(price/people))
else:
    print("NO?? So who is cooking!")

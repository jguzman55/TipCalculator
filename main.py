initbill = float(input("What is your initial bill?\n"))

tip = float(input('How much would you like tip? (in %) \n'))

people = int(input("How many people would you like to split the bill with?\n"))

total = round(tip / 100 * initbill + initbill, 2)

pplbill = total / people

final = round(pplbill, 2)

final = "{:.2f}".format(pplbill)

print(f"You chose to tip {tip}% of ${initbill}\n")
print(f"Your final bill after adding {tip}% in tip is ${total}\n")
print(f"When split into {people}, each person should pay ${final} of ${total}\n")

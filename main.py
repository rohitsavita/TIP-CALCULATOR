total_bill = float(input("What was the total bill (₹): "))

tip = float(input("How much tip would you pay (%): "))

if tip<0:
    print("Please enter a tip.")
else:
    people = int(input("How many people to split the bill: "))

    tp = (total_bill * tip) / 100

    s2 = (total_bill + tp) / people

    print(f"Each person should pay ₹{s2:.2f}")
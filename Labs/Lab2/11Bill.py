# calculate electricity bill based on following criteria. Which takes the unit from the user
un = int(input("Enter a units in electricity bill "))
bill = 0
if(un >= 0 and un <= 50):
    bill = (2.6 * un)
elif(un > 50 and un <= 100):
    bill = (2.6 * 50) + (3.25 * (un - 50))
elif(un > 100 and un <= 200):
    bill = (2.6 * 50) + (3.25 * 50) + (5.26 * (un - 100))
elif(un > 200):
    bill = (2.6 * 50) + (3.25 * 50) + (5.26 * 100) + (8.45 * (un - 200))
print("Electricity bill of ", un, "units is ", bill)

n=int(input("Enter a number (try 6 or 9): "))
guess=input("Is bit 0 of " + str(n) + " ON? (yes or no): ")
input("check the split bit. Press Enter ")
if n & 1:
    print(" ", n, " binary:", bin(n)[2:], " bit 0 ON - group A your guess: ", guess)
else:
    print(" ", n, " binary:", bin(n)[2:], " bit ) OFF - group B your guess:", guess)
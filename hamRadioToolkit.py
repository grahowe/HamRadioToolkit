"""
Date of last update: 1 November 2021
Author: Owen Graham, KE0SBX
See github page for README.txt
73 and happy operating! Hope to hear you on the air
"""
#Import datetime for UTC timestamp clock
import datetime

#Constants
constantft = 468.00
halfConstantft = 234.00
constantm = 143.00
halfConstantm = 71.50
ohmConstant = 50

#Menu options
choice = int(input("Enter 1 for dipole calculator, 2 for balun calculator, 3 for UTC clock, or 0 to quit: "))
while(choice != 0):
    
    
    #Half-wave Dipole Calculator choice
    if (choice == 1):
        print("\n************Welcome to the dipole calculator************")
        antChoice = int(input("\nEnter 1 for feet or 2 for meters: "))
        freq = float(input("\nEnter the frequency in MHz: "))
        #Choice of feet
        if (antChoice == 1):
            print("\nThe total length of your dipole (L) in feet is: " + str(round(constantft/freq, 2)) + " ft")
            #This can also be the total length of a quarter-wave dipole
            print("The total length of each element (E) in feet is: " + str(round(halfConstantft/freq, 2)) + " ft")
            choice = int(input("\nEnter 1 for dipole calculator, 2 for balun calculator, 3 for UTC clock, or 0 to quit: "))
        #Choice of meters    
        if (antChoice == 2):
            print("\nThe total length of your dipole (L) in feet is: " +str(round(constantm/freq, 2)) + " m")
            #This can also be the total length of a quarter-wave dipole
            print("The total length of your element (E) in feet is: " + str(round(halfConstantm/freq, 2)) + " m")
            choice = int(input("\nEnter 1 for dipole calculator, 2 for balun calculator, 3 for UTC clock, or 0 to quit: "))
            
            
    #Balun Calculator choice        
    if (choice == 2):
        print("\n************Welcome to the balun calculator************")
        ohmAnt = int(input("\nEnter the impedance of your feedline: "))
        print("\nThe impedance factor/SWR of your antenna based on a 50 ohm feedline system is: " + str(ohmAnt/ohmConstant) + ":1")
        print("You need a " + str(ohmAnt/ohmConstant) + ":1 balun for safe operation")
        choice = int(input("\nEnter 1 for dipole calculator, 2 for balun calculator, 3 for UTC clock, or 0 to quit: "))
        
    #UTC Clock
    if (choice == 3):
        print("\n************The current date and time is: ************")
        print("")
        print(datetime.datetime.utcnow())
        choice = int(input("\nEnter 1 for dipole calculator, 2 for balun calculator, 3 for UTC clock, or 0 to quit: "))
        
#Closing Message        
print("\n************Thank you and happy operating 73!************")
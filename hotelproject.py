# -*- coding: utf-8 -*-



#import csv module
#import random module
import csv
import random
#function to search bookings
def searchfilm():
    
    data=[]
    with open("cinema.csv") as csvfile:
        reader = csv.readder(csvfile)
        for row in reader:
            data.append(row)
    print(data)

    lookup = input("Please enter the film name: ")

    #loops through all data in column 4 assigns it to variable called 'co14'
    col4 = [x[3] for x in data]
    #print test if data in co14 is correct
    print(col4)

    if lookup in col4:

        #searches column 4 for instances of film name
        #if finds match, the index(row) # of the match is noted as 'k'
        #data[k] prints all the information on that row
        for k in range (0, len(col4)):
            if col4[k] == lookup:
                #print("test", k)
                print(data[k])
                #results.append(k)

    else:
        print("No film is listed under that title.")

#function to add bookings
def addbooking():  
    #2D array called bookings for collected data written to csv file
    bookings = []
    #creates random # for booking reference
    data = []
    with open("cinema.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    #set booking random # between 2 #s to test if works    
    bookingref = random.randint(35,37)
    #converts integer to string for writing to csv file
    bookingref = str(bookingref)
    #creates a loop through column zero into data
    col1 = [x[0] for x in data]
    #test if program looks at booking numbers
    print(col1)

    #If the booking ref exists in column 1 then do this
    if bookingref in col1:

        bookingref = int(bookingref)

        #code to make new booking ref
        bookingref2 = random.randint(1,1000)
        newbookingref = bookingref * bookingref2
        newbookingref = str(newbookingref)
        
        #prints the booking reference so the user can see it
        print("The booking ref is:", bookingref)

        #prompting user for input
        firstname = input("May we please have your First Name?: ")
        lastname = input("Thank You. And your Last Name?: ")
        print ()
        film = input("Please enter the film you wish to view: ")
        day = input("What day of the week would you like to attend this film?: ")

        #add more details to 2d array -- appending or add variable name to bookings

        bookings.append(bookingref)
        bookings.append(firstname)
        bookings.append(lastname)
        bookings.append(film)
        bookings.append(day)

        #adding details to the 2d array called bookings and writes to csv file
        with open("cinema.csv","a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(bookings)
    #If the booking ref is not in column 1 (0) then continue as normal
    else:

        print("The booking reference number is:", bookingref)
        firstname = input("May we please have your First Name?: ")
        lastname = input("Thank You. And your Last Name?: ")
        print ()
        film = input("Please enter the film you wish to view: ")
        day = input("What day of the week would you like to attend this film?: ")

        bookings.append(bookingref)
        bookings.append(firstname)
        bookings.append(lastname)
        bookings.append(film)
        bookings.append(day)

        with open("cinema.csv","a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(bookings)
      
#Menu System

print("Welcome to the Cinema Ticket Booking System.")
print () 
print("Select an option from the menu below to continue.")
print ()
print("Press 1 to book a film")
print ()
print("Press 2 to search by film name")
print ()
choice = input("Please select and option from above.: ")

if choice == "1":
    addbooking()

elif choice == "2":
    print("test print statement to see if choice 2 works")

else:
    print("Sorry, that is an Invalid Entry")

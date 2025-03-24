#Tyson Blatter 1-24-25 4.2
#the function that converts miles to kilometers
def miles_to_kilometers(miles):
    return miles * 1.60934

# the main part of the program
while True:
    try:
           miles = float(input("Enter the number of miles driven: "))
           #catches illogical numbers
           if miles < 0:
               print("Miles cannot be a negative number. Please enter a valid number.")
               continue

# this is what the user will see
           kilometers = miles_to_kilometers(miles)
           print(f"You have driven: {miles} miles.")
           print(f"That's about: {kilometers:.2f} kilometers.")
           break
           #typing anything but a number will be asked to try again.
    except ValueError:
        print("Please enter a valid number.")
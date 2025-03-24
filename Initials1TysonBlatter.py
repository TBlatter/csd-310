#Tyson Blatter 2-15-25 6.2
#grabs users full name
full_name = input("Enter full name: ")
#this code breaks up the name
split_name = full_name.split()
#this code takes the first initial of each part of the name and adds a period.
initials = [name[0] + "." for name in split_name]
#puts them all together and shows it to the user.
print(" ".join(initials))
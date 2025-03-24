#Tyson Blatter 3-23-2025 1-3
def beer_song(bottles):
    #make a loop for the number of bottles
    for i in range(bottles,0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottle(s) of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, 0 bottles of beer on the wall.\n")

    #once the number is zero it's time to end the song
    print("Time to buy more bottles of beer.")

num_bottles = int(input("Enter number of bottles: "))
beer_song(num_bottles)
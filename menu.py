import handleCSV
import os

def menu():
    print("Welcome to the Automatic Youtube Playlist Generator!")
    print("What playlist would you like to copy from:")
    initial_count = 1
    dir = "data"
    dic = {}
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            print("{}: {}".format(initial_count, path))
            dic[initial_count] = os.path.join(dir, path)
            initial_count += 1
    return dic

def get_data():
    dic = menu()
    valid = False
    while not valid:
        try:
            choice = int(input("Please enter your choice: "))
            valid = True
        except ValueError:
            print("Not a valid choice.")
    return handleCSV.df_tracks(dic[choice])

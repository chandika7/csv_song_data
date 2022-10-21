import csv

with open("charts.csv") as file:
    csv_reader = csv.reader(file)


def main():
    menu()


def menu():
    print("COM709 Assiment -Designing and Developing Computer Programs")
    print("--------------------------------------------------------------")

    choice = int(input("""
                      1: Retrieve the details for the top ranked song for a particular day
                      2: Retrieve the details of the artist with the most top ranked songs
                      3: Retrieve the details of the 10 songs with the longest number of weeks on the board
                      4: Retrieve the song that has moved the most in ranking on the board
                      5: Visualise the top songs
                      0: Exit

                      Please enter your choice: """))

    if choice == 1 :
        top_ranked_song()
    elif choice == 2 :
        top_ranked_song_artist()
    elif choice == 3 :
        songs_longest_number_weeks()
    elif choice == 4 :
        most_ranking_board()
    elif choice == 5:
        Visualise_top_songs()
    elif choice == 0:
        quit()
    else:
        print("You must select number 1 to 5 or 0 for exit")
        print("Please try again")
        menu()


def top_ranked_song():
    print("Retrieve the details for the top ranked song for a particular day")
    pass

def top_ranked_song_artist():
    print("Retrieve the details of the artist with the most top ranked songs")
    pass

def songs_longest_number_weeks():
    print("Retrieve the details of the 10 songs with the longest number of weeks on the board")
    pass

def most_ranking_board():
    print("Retrieve the song that has moved the most in ranking on the board")
    pass

def Visualise_top_songs():
    print("Visualise the top songs")
    pass


# the program is initiated
main()

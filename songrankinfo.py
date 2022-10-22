import csv
import matplotlib
from matplotlib import pyplot
import unittest
import pandas

#with open("charts.csv","r") as file:
csv_reader = pandas.read_csv('charts.csv')
#csv_reader = pandas.read_csv('charts.csv',index_col='Song',
#            parse_dates=['date'],
#            header=0,
#            names=['date','rank','Song', 'artist','last-week','peak-rank','weeks-on-board'])

#print(csv_reader1)

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
#    print(csv_reader)
    sub_listrank= csv_reader[csv_reader['rank'] ==1]
    sub_listrank2=(sub_listrank.drop_duplicates(subset=['date']))
    blankIndex=[''] * len(sub_listrank2)
    sub_listrank2.index=blankIndex
    print(sub_listrank2[['date','song']])
#print(df[['name', 'score']])
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
    data = (3, 6, 9, 12, 15)
    fig, simple_chart = matplotlib.pyplot.subplots()
    simple_chart.plot(data)
    matplotlib.pyplot.show()
    pass


# the program is initiated
#main()
top_ranked_song()
#Visualise_top_songs()
#unittest.main()
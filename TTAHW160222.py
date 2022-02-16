# Task 1

# Create a CSV file of 15 holiday destinations for a website
# 1. Add in a column of destinations
# 2. Add in a column that shows feedback score out of 10 for that destination
# 3. Add in a column for average hotel star rating for those destinations
# 4. Add in a column for number of all-inclusive hotels within each destination
# 5. Add in the most visited city in each destination

# [SEE GIT READ ME FOR REFERENCE PHOTO]

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':

# Task 2

    # Importing my holidaysDestinations File.
    holidayDestinations = pd.read_csv("D:\Documents\Tech Talent Academy Bootcamp\HolidayDestinations.csv")
    print("Holiday Destinations Data Set: \n ", holidayDestinations)

    # 1. How many rows and columns are there in your file? - There are 14 rows and 5 column in my file.
    print("Number of ros and columns in my dataset: ", holidayDestinations.shape)

    # 2. Print row 3-8 ( using iloc/loc).
    print("Observing rows 3 to 8: \n", holidayDestinations[2:8])

    # 3. Find the mean number of all-inclusive hotels across all destinations.
    print("The mean number of all hotels across all destinations is: ", holidayDestinations["Near_By_Hotels"].mean())

    # 4. Find the lowest scoring destination.
    print("The lowest scoring destination has a score of: ", holidayDestinations["Review_Score"].min())
    destination = holidayDestinations["Review_Score"].idxmin()
    print("The associated destination with the lowest score is: ", destination)
    print("The lowest Scoring Destination is: ", holidayDestinations.iloc[destination, 0])

    # 5. Find the highest scoring destination.
    print("The highest scoring destination has a score of: ", holidayDestinations["Review_Score"].max())
    destination2 = holidayDestinations["Review_Score"].idxmax()
    print("The associated destination with the highest score is: ", destination2)
    print("The highest Scoring Destination is: ", holidayDestinations.iloc[destination2, 0])

    # 6. Find all the destinations where there are more than 50 all-inclusive hotels.
    top50hotelsFilter = holidayDestinations["Near_By_Hotels"] >= 50
    destinationWithTop50Hotels = holidayDestinations[top50hotelsFilter]
    print("The destinations with the more than 50 hotels: \n", destinationWithTop50Hotels)

    # 7. Filter the data by score above 8.
    reviewScoreAbove8Filter = holidayDestinations["Review_Score"] >= 8
    allDataAboveAScoreOf8 = holidayDestinations[reviewScoreAbove8Filter]
    print("Filtered data with a score above 8: \n", allDataAboveAScoreOf8)

    # 8. Filter the data score below 3 ( I need to know if these destinations should be removed or there is a problem)
    reviewScoreBelow3Filter = holidayDestinations["Review_Score"] <= 3
    allDataBelowAScoreOf3 = holidayDestinations[reviewScoreBelow3Filter]
    print("Filtered data with a score below 3: \n", allDataBelowAScoreOf3)

# Extension Tasks

# 1. Is there a correlation between number of all-inclusive hotels and score? [SEE GIT READ ME FOR GRAPH PHOTO]

    holidayDestinations.plot.scatter(x='Near_By_Hotels', y='Review_Score', color='black')
    plt.title("Hotels and Scores")
    plt.xlabel("Number of Hotels")
    plt.ylabel("Score")
    sns.regplot(x=holidayDestinations['Near_By_Hotels'], y=holidayDestinations['Review_Score'],
                scatter_kws={"color": "black"}, line_kws={"color": "red"})
    plt.show()
    print("The more hotels there were the higher the overall score was. As we can "
          "see with the positive correlation in the scatter graph.")

# TODO: Google how to do correlations in python pandas - DONE
# TODO: lmplot() creates a separate table from my initial inputted data. I dont want 2 graphs created only 1. - DONE
# TODO: How to change correlation line colour and plot point colours. - DONE
# TODO: How to underline the title? - IN PROGRESS

# 2. Create a data visualisation diagram to show destination and highest scores? [SEE GIT READ ME FOR GRAPH PHOTO]

    holidayDestinations.plot.barh(y='Review_Score', x='Holiday_Destinatinos', color='#77dd77')
    plt.title("Holiday Destinations and their Scores")
    plt.xlabel("Review Score")
    plt.ylabel("Holiday Destinations")
    plt.tight_layout()
    plt.show()

#-------------------------TERMINAL OUTPUT----------------------------#

# Holiday Destinations Data Set:
#           Holiday_Destinatinos  Review_Score  ...  Near_By_Hotels  Most_Visited_Cities
# 0             United Kingdom             8  ...             104               London
# 1                      Japan            10  ...              78                Tokyo
# 2   United States of America             6  ...              89             New York
# 3                      India             7  ...              21               Mumbai
# 4                  Australia             9  ...              32             Canberra
# 5                      China             7  ...              14            Hong Kong
# 6                      Italy             8  ...              67                 Rome
# 7                       Bali             8  ...              46             Denpasar
# 8                   Thailand             7  ...              22              Bangkok
# 9            The Netherlands             9  ...              16           Amsterdam
# 10               North Korea             3  ...               2            Pyongyang
# 11                     Egypt             7  ...              13                Cairo
# 12                   Ireland             4  ...               9               Dublin
# 13                    France             6  ...              74                Paris
#
# [14 rows x 5 columns]
# Number of ros and columns in my dataset:  (14, 5)
# Observing rows 3 to 8:
#         Holiday_Destinatinos  Review_Score  ...  Near_By_Hotels  Most_Visited_Cities
# 2  United States of America             6  ...              89             New York
# 3                     India             7  ...              21               Mumbai
# 4                 Australia             9  ...              32             Canberra
# 5                     China             7  ...              14            Hong Kong
# 6                     Italy             8  ...              67                 Rome
# 7                      Bali             8  ...              46             Denpasar
#
# [6 rows x 5 columns]
# The mean number of all hotels across all destinations is:  41.92857142857143
# The lowest scoring destination has a score of:  3
# The associated destination with the lowest score is:  10
# The lowest Scoring Destination is:  North Korea
# The highest scoring destination has a score of:  10
# The associated destination with the highest score is:  1
# The highest Scoring Destination is:  Japan
# The destinations with the more than 50 hotels:
#          Holiday_Destinatinos  Review_Score  ...  Near_By_Hotels  Most_Visited_Cities
# 0             United Kingdom             8  ...             104               London
# 1                      Japan            10  ...              78                Tokyo
# 2   United States of America             6  ...              89             New York
# 6                      Italy             8  ...              67                 Rome
# 13                    France             6  ...              74                Paris
#
# [5 rows x 5 columns]
# Filtered data with a score above 8:
#    Holiday_Destinatinos  Review_Score  ...  Near_By_Hotels  Most_Visited_Cities
# 0       United Kingdom             8  ...             104               London
# 1                Japan            10  ...              78                Tokyo
# 4            Australia             9  ...              32             Canberra
# 6                Italy             8  ...              67                 Rome
# 7                 Bali             8  ...              46             Denpasar
# 9      The Netherlands             9  ...              16           Amsterdam
#
# [6 rows x 5 columns]
# Filtered data with a score below 3:
#     Holiday_Destinatinos  Review_Score  ...  Near_By_Hotels  Most_Visited_Cities
# 10          North Korea             3  ...               2            Pyongyang
#
# [1 rows x 5 columns]
# The more hotels there were the higher the overall score was. As we can see with the positive correlation in the scatter graph.
#
# Process finished with exit code 0


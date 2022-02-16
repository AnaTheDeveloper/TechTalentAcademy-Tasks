import pandas as pd

# Pandas is a library that facilitates data manipulation, visualisation and analysis.
# Pandas build upon NumPy.
# They key concepts of Pandas are indexing and dataframes.
# A dataframe is a two-dimensional tabular data structure.
# A series is the name for a one-dimensional data structure used within Pandas. If you do not assign an index to your series, Pandas will automatically assign one

if __name__ == '__main__':

    # One dimensional array.
    mySeries = pd.Series([439, 98.54, 'Hello World', 'Sea Breeze', -342])
    print("This is my one dimensional array: \n", mySeries)

    # Creating a Dataframe.

    # 1. Create the data set first. This uses a dictionary.
    inventory = {"Code": [475984412, 475871129, 476214584, 475854812],
                 "Produce": ["Avocado", "Banana", "Courgette", "Cauliflower"],
                 "Origin": ["Mexico", "Costa Rica", "France", "UK"],
                 "Price": [1.75, 0.73, 2.00, 1.80]}

    print("This is my data set: \n", inventory)

    # 2. Assigning the dataset to the DataFrame layout using Pandas
    myframe = pd.DataFrame(inventory)
    print("This is what my dataframe looks like: \n", myframe)

    # 3. You can also introduce an index that's the UID.
    myframe.index = ["AV", "BN", "CG", "CF"]    # When creating an index, be aware that the index values need to be unique
    print("My data frame with a unique index: \n", myframe)

    # Importing existing data using pandas

    # 1. Read the CSV file using pd.read_csv
    vetData = pd.read_csv("D:\Documents\Tech Talent Academy Bootcamp\Pandas - Vet Data.csv") # or Filename.csv also works
    # Ensure that your csv file in within the same folder as your python file
    print("I imported this external data from a CSV file and this is it: \n", vetData)

    # Retrieve Data from the dataset

    # 1. Retrieve a series
    print("Retieves a series of data from the data set: \n", vetData["Pet_Age"])

    # 2. Retrieve specific data as a dataframe.
    print("Retrieved a whole section from the dataset as a dataframe: \n", vetData["Pet_Name"])

    # 3. Retrieve multiple columns as a dataframe.
    print("Retrieved multiple columns as a dataframe: \n", vetData[["Type", "Pet_Age", "Chipped"]])

    # 4. Temporarily removes data from the dataset. It just hides it.

    # print("Deleting this row from the dataset: \n", vetData.drop([6])

    # 5. Retrieve data bases on index
    print("Retrieved data based on index requirement: \n", vetData.loc[vetData.Pet_Name == "Monty"])

    # Observe specific rows of data

    # 1. Observe the first 4 rows of data.
    print("Observing the first 4 rows of data: \n", vetData[0:4])

    # 2. Observing the 9th, 11th and 12th observations.
    print("Observing the 9th, 11th, and 12th observations: \n", vetData[8:12])

    # LOC and ILOC for data selection

    # iloc: Retrieves data based on index location.
    # loc: Retrieves data based on labels attributed to that data.

    # iloc example
    print("Using iloc im printing out the observations for index row 1: \n", vetData.iloc[[0]])

    # loc example
    vetData2 = pd.read_csv("D:\Documents\Tech Talent Academy Bootcamp\Pandas - Vet Data.csv", index_col="Owner_Surname")
    print("Using loc im getting specific information: \n", vetData2.loc[["Smith", "Sorola"]])

    # Printing CColumns and Ranges using iloc

    # To select specific rows and columns using iloc, you can separate these with a comma. Rows always come first.
    # For example, using data.iloc[7, 4] will retrieve you the data that is in the 8th row and the 5th column.
    print("Retrieving specific rowas and columns: \n ", vetData.iloc[[7, 4]])

    # To print a range using iloc, you can use a colon (:).
    # For example, to print rows 4-7 and columns 3-4, you will need the following code: dataSetName.iloc[3:7, 2:4]
    print("Retrieving data in a range: \n ", vetData.iloc[3:7, 2:4])

    # Another way of creating a dataframe. Not using a dictionary.

    frame = pd.DataFrame([[8.96, 1884], [7.87, 1149], [7.13, 428]],
                         index=["Copper", "Iron", "Zinc"],
                         columns=["Density g/cm3", "Melting Point BC"])
    print("Dataframe example 2: \n", frame)

    print("Retrieved all the information from Copper: \n", frame.loc[["Copper"]])

    # Working with a larger data set
    largerDataSetExample = pd.read_csv("D:\Documents\Tech Talent Academy Bootcamp\Pandas - Ign Data.csv")

    # See how many rows and columns this data set has
    print("This larger bit of data has these many rows and columns: ", largerDataSetExample.shape)

    # Looking at the head and tail of a dataset

    print("Printing the head: \n ", largerDataSetExample.head(5))

    print("Printing the tail: \n ", largerDataSetExample.tail(5))

    # Pandas Series Objects
    #print("Printing specific data from the data set: ", largerDataSetExample["platform"])

    # Mathematical Operations on the dataset
    print("Get the mean of the Score column: ", largerDataSetExample["score"].mean())

    # print("Divides every value in the column by 2: ", largerDataSetExample["score"] / 2)
    # print("Multiplys every value in the column by 10: ", largerDataSetExample["score"] * 10)

    # Boolean Indexing
    myFilter = largerDataSetExample["score"] > 8
    print("Boolean indexing of every score under 8 for the first 15 rows: ", myFilter.head(15))

    # Creating filters
    highscore = largerDataSetExample[myFilter]
    print("Created a filter: \n", highscore.head())

    # Using multiple filters
    top_ipad_filter = (largerDataSetExample["score"] > 8) & (largerDataSetExample["platform"] == "iPad")
    multipleFilters = largerDataSetExample[top_ipad_filter]
    print("Multiple filter example: \n", multipleFilters.head(3))

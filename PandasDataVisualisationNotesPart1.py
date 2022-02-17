import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# In Pandas, you can also create visualisations. These include:
# • Line Plot
# • Scatter Plot
# • Area Plot
# • Bar Chart
# • Pie Chart
# • Histogram
# • Kernel Density Function
# • Box Plot
# • Scatter Matrix Plot

if __name__ == '__main__':

    # -------------------Tips & Tricks---------------- #

    # Import matplotlib.pyplot as plt

    # Create a Title for graph: plt.title("Hotels and Scores")

    # Create a x axis label: plt.xlabel("Number of Hotels")

    # Create a y axis label: plt.ylabel("Score")

    # Scatter graph: dataSetName.plot()/.line()/.bar()/.barh()/.pie()   (x='nameOfDataSetSection', y='nameOfOtherDataSetSection')

    # Chart Customisation
    # Determine graph type: kind='scatter'
    # Change colour: color='red' or '#143sdf34'
    # Change figure size: figsize=(7, 7),
    # Add a percentage value: autopct='%1.1f%%'
    # Everything is rotated counter-clockwise by 90 degrees: startangle=90
    # Rotate Text: rotation=45





    # Scatter graph
    gdp_cal = pd.DataFrame({
        'GDP_growth': [6.1, 5.8, 5.7, 5.7, 5.8, 5.6, 5.5, 5.3, 5.2, 5.2],
        'Oil_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
    })
    df = pd.DataFrame(gdp_cal, columns=['Oil_Price', 'GDP_growth'])
    print(df)
    df.plot(x='Oil_Price', y='GDP_growth', kind='scatter', color='red')
    plt.show()

    # Line Graph
    inf_cal = {'Year': [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011],
               'Inflation_Rate': [5.8, 10, 7, 6.7, 6.8, 6, 5.5, 8.2, 8.5, 9, 10]
               }
    data_frame = pd.DataFrame(inf_cal, columns=['Inflation_Rate'],
                              index=[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011])
    data_frame.plot.line()

    plt.title('Inflation Rate Summary of Past 11 Years')
    plt.ylabel('Inflation_Rate')
    plt.xlabel('Year')
    plt.show()

    # Bar Chart Vertical
    lit_cal = {
        'Country_Names': ['Pakistan', 'USA', 'China', 'India', 'UK', 'Austria', 'Egypt', 'Ukraine', 'Saudia',
                          'Australia',
                          'Malaysia'],
        'litr_Rate': [5.8, 10, 7, 6.7, 6.8, 6, 5.5, 8.2, 8.5, 9, 10]
    }
    data_frame = pd.DataFrame(lit_cal, columns=['Country_Names', 'litr_Rate'])
    print(data_frame)
    data_frame.plot.bar(x='Country_Names', y='litr_Rate')
    plt.show()

    # Bar Chart Horizontal
    data_chart = {'litr_Rate': [5.8, 10, 7, 6.7, 6.8, 6, 5.5, 8.2, 8.5, 9, 10]}
    df = pd.DataFrame(data_chart, columns=['litr_Rate'],
                      index=['Pakistan', 'USA', 'China', 'India', 'UK', 'Austria', 'Egypt', 'Ukraine', 'Saudia',
                             'Australia',
                             'Malaysia'])

    df.plot.barh()

    plt.title('Literacy Rate in Various Countries')
    plt.ylabel('Country_Names')
    plt.xlabel('litr_Rate')
    plt.show()

    # Pie Chart
    material_per = {'Earth_Part': [71, 18, 7, 4]}
    dataframe = pd.DataFrame(material_per, columns=['Earth_Part'], index=['Water', 'Mineral', 'Sand', 'Metals'])

    dataframe.plot.pie(y='Earth_Part', figsize=(7, 7), autopct='%1.1f%%', startangle=90)
    plt.show()

    # NOTES FROM POWER-POINT BELOW

# Line plot: df.plot()
# Scatter plot: df.plot.scatter(x='sepal length (cm)', y='sepal width (cm)') or df.plot.scatter(x='sepal length (cm)', y='petal length (cm)')
# Area PLot: columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
# df[columns].plot.area()
# Bar Chart: df.groupby('species').mean().plot.bar()
# Pie Chart: df.groupby('species').count().plot.pie(y='sepal length (cm)')
# Histogram: df.hist(figsize = (5,9))
# Kernal Density Function: df.plot.kde(subplots=True, figsize=(5,9))
# Box Plot: columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
# df[columns].plot.box()
# #plt.xticks(rotation='vertical') # required to work: import matplotlib as plt
# from pandas.plotting import scatter_matrix
# scatter_matrix(df, figsize=(10, 10))

# ---------------------EXAMPLE CHARTS FROM STACK OVERFLOW------------------------#

    cols = ['Date', 'Brake Hrs',  'Tram Hrs',  'Brake%',  'Tram%',  'Br/Tr%']
    data_frame = pd.DataFrame([['Mon',       0.87,      4.26,   16.90,  83.10,   20.33],
                                ['Tue',       1.00,      3.05,   24.66,  75.34,   32.73],
                                ['Wed',       1.77,      3.87,   31.44,  68.56,   45.85],
                                ['Thu',       1.86,      5.16,   26.44,  73.56,   35.94],
                                ['Fri',       1.41,      2.01,   41.15,  58.85,   69.93],
                                ['Sat',       0.01,      5.03,    0.14,  99.86,    0.14],
                                ['Sun',       0.40,      1.16,   25.82,  74.18,   34.82]],
                             columns = cols)



    f, ax1 = plt.subplots(1, figsize=(10, 5))

    # Set the bar width
    bar_width_tram = 1
    bar_width_brake_percentage = 1

    # Positions of the left bar-boundaries
    bar_l = [i + 1 for i in range(len(data_frame['Tram Hrs']))]

    # Positions of the x-axis ticks (center of the bars as bar labels)
    tick_pos = [i + (bar_width_tram / 2) for i in bar_l]

    # Define the colours for the corresponding
    # bars in the graph
    tram_data_hrs_colour = '#00AC00'   # Green
    bd_per_colour = '#DA0505'   # Red

    # Create a bar plot, in position bar_1
    ax1.bar(bar_l,
            # using the pre_score data
            data_frame['Tram Hrs'],
            # get rid of border lines
            edgecolor="none",
            # set the width
            width=bar_width_tram,
            # with the label pre score
            label='Tramming Hours',
            # with alpha 0.5
            alpha=0.05,
            # with color
            color=tram_data_hrs_colour,
            align = 'center')


    # Set the X-ticks with dates
    plt.xticks(tick_pos, data_frame['Date'])

    plt.yticks(np.arange(0, 15, 3))

    # Set the labels and legend
    ax1.set_ylabel("Tramming Time (Hours)")
    ax1.set_xlabel("Previous Week")

    # Second axis
    ax2 = ax1.twinx()
    ax2.set_ylabel("Braking to Tramming  (%)")

    plt.plot(bar_l,data_frame['Brake%'], '-', label='Relative Braking Percentage')

    plt.yticks(np.arange(0, 250, 50))

    # Set the title of the chart
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc=2)

    plt.xlim(0, len(tick_pos) + 1)
    plt.show()




























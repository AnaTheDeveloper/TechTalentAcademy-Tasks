import pandas as pd
import matplotlib.pyplot as plt

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





























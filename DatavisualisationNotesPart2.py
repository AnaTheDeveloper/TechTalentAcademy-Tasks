import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Visual Analytics combines analytics with data visualisation in order to solve problems. It is an interdependent
# process where the visualisations drive analytical models, and the models influence the visualisations.

# 1. Everything starts with what the user wants to do
# 2. Visual analytics started off in the computer visualisation community
# 3. Many of its evaluation models and methods apply

# Data Types: Continuous(quantitative data), ordered(Mon,Tues, Wed) and categorical(fruit, veg).
# Marks: Basic graphical elements of an image. Can be 0D, 2D, 3D. Points, lines and areas.

# Visuals using Altair -  pip install altair vega_datasets

# There are many concepts in Altair Official User Guide, but Data, Marks and Encodings are the basic. Understanding
# the following concepts should be enough for you to create basic interactive charts.

# The data used internally by Altair is stored in Pandas DataFrame format, but there are many ways to pass it in as a:
# • Pandas Data Frame
# • Data or related object
# • URL string pointing to a json or csv formatted file

import altair as alt
import pandas as pd
from vega_datasets import data as carDataExample

if __name__ == '__main__':

    # pip install altair-viewer
    # https://altair-viz.github.io/user_guide/compound_charts.html

    # Stair like graph display
    dataExample1 = pd.DataFrame({'col-1': list('CCCDDDEEE'),
                         'col-2': [2, 7, 4, 1, 2, 6, 8, 4, 7]
                         })

    chart = alt.Chart(dataExample1).mark_point().encode(x='col-1', y='col-2').interactive()
    # chart.show()

    # Using external data sets
    cars = carDataExample.cars()
    brush = alt.selection_interval()

    points = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
    ).add_selection(
        brush
    )
    # points.show()

    # Bar chart in Altair
    bars = alt.Chart(cars).mark_bar().encode(
        y='Origin:N',
        color='Origin:N',
        x='count(Origin):Q'
    ).transform_filter(
        brush
    )
    # bars.show()

    # Point and bar chart together
    points2 = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray')),
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).add_selection(
        brush
    )

    bars2 = alt.Chart(cars).mark_bar().encode(
        y='Origin:N',
        color='Origin:N',
        x='count(Origin):Q',
    ).transform_filter(
        brush
    )
    show2Graphs = alt.vconcat(points2, bars2) # or hconcat which puts the graphs next to each other
    show2Graphs.show()

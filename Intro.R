print("Hello World")

# Assign Variables - Shot cut is ALT -

personsName <- "username"

# Readline for user input
# Readline is a built-in function that accepts a string argument within its 
# parentheses to output as a prompt. It waits for user to type in the input 
# to assign to that variable.

name <- readline("What is your name?")

# The paste function concatenates a string and an assigned variable to be output.

hello <-  paste("Welcome", name)
print(hello)

# Data types in R:
# Character - String
# Double - Float or decimal
# Integer - Whole Numbers
# Logical - True or false

# To find out the data type you can use the typeof() function.
title <-  "Women in Data"
type <- paste("Title of Type: ", typeof(title))
print(type)

#1D data types
# vectors
# lists

#2D data types
# matrix
# data frame

#vectors - can store multiple values but MUST be the same data type
my_vec <-c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
my_vec
my_vec[1]
my_vec[3] <- "Saturday"
my_vec


#lists - can store mixed data types
info <- list(21L, 165.00, "Lisa", TRUE)
info

info <- list(age=21L, height=165L, name="Lisa", employed=TRUE) 
info
info["name"]

info["airport"] <- "JFK"

# When you create any R code to store data in any structure such as a variable or a list, a data structure object is 
# created in the RStudio environment. You can use the built-in ls() function to call all objects/variables within the 
# current console environment.

airport.codesUk <- list("Birmingham" = "BHX", "London Heathrow" = "LHR", "Bristol " = "BRS", "Manchester" = "MAN")
airport.dubai <- "DBX"
airport.sanfran <- "SFO"

ls()
rm(airport.sanfran)
ls()

# Arithmetic Operations
num1 <- 10
num2 <- 4

num1 + num2
num1 - num2
num1 * num2

5**2
6.5/2

# Comparison operators.
# Equality ==
# Inequality !=
# Greater than >
# Greater than or equal to >=
# Less than <
# Less than or equal to <=

nil <- 0
num <- 0
max <- 1

nil != max
nil > max
nil < max

# If statements and else statements

if (5 > 1) {
  print ("five is greater than one")
} 


number <- 15

if (number < 10) {
  print("Number is less than 10")
} else if (number == 15) {
  print("We are bang on!")
} else {
  print("Number is greater than ")
}

# Power of R allows you to provide graphic depictions of data stored within R script structures.
# Basic plotting. You can conduct basic plots in R without importing a library
x <- c(1, 3, 4, 5, 6)
y <- c(21, 5, 7, 9, 3)

plot(x, y)

plot(x, y, type="o")

?plot

# Adding more visual parameters

firstQ  <- c(Jan=2000, Feb=1200, Mar=2700)
secondQ <- c(Apr=1600, May=2500, June=3100)
thirdQ  <- c(Jul=4250, Aug=3600, Sep=3000)
fourthQ <- c(Oct=2100, Nov=1900, Dec=3560) 

# Combining all 4 vectors

wholeYear <- c(firstQ, secondQ, thirdQ, fourthQ)
wholeYear

# Plotting vectors - specifying type, colour and point of characters.  
# pch = point character of the points on the graph 
plot(wholeYear, type ="o", col="blue", pch=16)

# Turning off annotation and axes labels.

plot(wholeYear, type ="b", col="blue", pch=1, xaxt="n", xlab="Months", ylab="Sales")

# Adding range and annotation for x and y axis

axis(1, at=1:12, lab=names(wholeYear))

# Add titles 
title(xlab= "Month", ylab = "Sales", main = "Yearly Sales Figures", col.main="Red")

# Matrix
data <- seq(1:32)
my_matrix <- matrix(data, nrow=4, ncol=8)
my_matrix

print(data)

ny <- c(3.8,5.5,9.9,15.7,21.5,26.3)
la <- c(19.5,19.4,19.7,20.8,21.3,22.7)
sf <- c(13.7,15.4,20.0,24.6,28.5,32.7)

combined_mat <- rbind(ny,la,sf)
combined_mat

matplot(combined_mat, type ="o", pch=15, col=1:3)

# Data frames
city <- c("NY", "LA", "Vegas")
rainfall <- c(20L, 10L, 5L)
sun <- c(FALSE, TRUE, TRUE)

frame <- data.frame(city, rainfall, sun)  

print (frame)

# In built data sets

# gglot2 is a library that can be used to create more sophisticated plots
# Ggplot Data sets:
# diamonds → Prices of over 50,000 round cut diamonds
# economics → US economic time series
# economics_long → US economic time series
# faithfuld → 2
# nd density estimate of Old faithful data
# luv_colors → ‘colors()’ in Luv space. Mapping between assorted color spaces
# midwest → Midwest demographics
# mpg → Fuel economy data from 1999 to 2008 for 38 popular models of cars
# msleep → mammals sleep dataset
# presidential → Terms of 11 presidents from Eisenhower to Obama
# seals → Vector field of seal movements
# txhousing → Housing sales in Texas

install.packages("ggplot2")
library(ggplot2)

# Find a toy data set
data(package = "ggplot2")

# Scatter plot with qplot

ggplot2::mpg

qplot(data = mpg, x = cty, y = hwy, geom = "point", color = class)

# Bar plot and stacked bar plot

ggplot2::diamonds

?diamonds
diamonds

qplot(data = diamonds, y = clarity, geom = "bar", fill = cut)

# Different graphs using geom ="graphType"
# "bar“ First tabulates frequencies of each value, then makes a barplot.
# "histogram“ Makes a histogram.
# "point“ Makes scatterplots. 
# "line" Makes a line plot. 
# "boxplot“ Makes a boxplot. 
# "density“ Makes the density plot 
# "smooth“ Fits a smooth line to a cloud of points and plots the output. 
# "dotplot“ Makes a dotplot.

library(tidyverse)
mpg

# Display on the x-axis and hwy on the y-axis:
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy))

# Adding colour to data points
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, color = class))

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy), color = "blue")


# Changing size of data points
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, size = class))

# Aplha changes transparency of points
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, alpha = class))

# Changing data points shape
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, shape = class))

# Bar chart
ggplot(data=mpg, aes(x=manufacturer, y=cty)) +
  geom_bar(stat="identity", width=0.5)

# Changing colors
ggplot(data=mpg, aes(x=manufacturer, y=cty)) +
  geom_bar(stat="identity", color="blue", fill="white")

# Minimal theme + blue fill color
ggplot(data=mpg, aes(x=manufacturer, y=cty)) +
  geom_bar(stat="identity", fill="steelblue")+
  theme_minimal()





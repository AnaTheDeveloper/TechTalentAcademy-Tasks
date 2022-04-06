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





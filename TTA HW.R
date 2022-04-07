# --------------------------------------Homework Project

# Imagine the following scenario: You are a data analyst at an organisation. You 
# have been given a data set and asked to create a meaningful data visualisation using this data.
# 
# Using the ggplot in-built data sets in RStudio and the qplot
# function, get your creative juices flowing and create a meaningful 
# and impactful data visualization using your preferred data set.

# Seeing what inbuilt datasets are available to me.
data(package = .packages(all.available = TRUE))

# Install ggplot2
install.packages("ggplot2")

# Select dataset.
library(ggplot2)

data(package = "ggplot2")

datasets::midwest

# Looking at the dataset.

head(midwest, 5)

names(midwest)

str(midwest)

summary(midwest)

?midwest  

# This dataset focuses on the population, economic and education level of 5 states.
# I want to data of Midwest Region demography to answer few basic questions related with 
# education, population and poverty.

# 1. Looking at each of the 5 states and their population sizes.

p <- ggplot(data = midwest, aes(x = state, y = poptotal, fill=state)) + geom_bar(stat="identity") + 
  xlab("Midwest States") + ylab("Total Population")+ ggtitle("Midwest States Vs. Total Population")
plot(p)

# 2. Looking at the relationship between the area vs population.
p <- ggplot(midwest, aes(x=area, y=poptotal)) + geom_point(aes(col=state, size=popdensity)) + 
     geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
     labs(subtitle="Area Vs Population", y="Population", x="Area", title="Scatterplot", caption = "Source: midwest")
plot(p)

# 3. Does education have an impact on poverty
p <- ggplot(data = midwest, aes(y = percbelowpoverty, x = percollege)) 
p + geom_point((aes(color = state))) + ggtitle("College Education Vs Total Poverty") + xlab("Percent College Educated") + 
  ylab("Percentage of Total poverty")
# 4. Education level and how this impacts poverty in each state.
p + geom_point(aes(color = state)) + geom_smooth(method = "lm", se=FALSE, color="black", formula = y ~ x) + 
  facet_wrap(~state) + ggtitle("College Education Vs Total Proverty by Each Midwest State") + 
  xlab("Percent College Educated") + ylab("Percentage of Total proverty") 

# 5. Using the map feature

library(usmap)
data(package = "usmap")
usmap::plot_usmap

df <- data.frame(state = c("IL", "IN", "MI", "OH", "WI"), values = c(12, 18, 23, 24, 78))

plot_usmap(data = df, values = "state", include = .east_north_central) + labs(title = "Midwest States")


# --------------------------------------Homework

# 1. - Write an R program to create three vectors a, b, c with 5 integers. 
#    - Combine the three vectors to become a 3×5 matrix where each column represents a vector. 
#    - Print the content of the matrix. 
#    - Plot a graph and label correctly.

a <- c(76, 45, 32, 56, 21)
b <- c(33, 76, 55, 88, 11)
c <- c(9, 12, 64, 92, 25)

data <- cblind(a, b, c)

my_matrix <- matrix(data, nrow=3, ncol=5)

print(my_matrix)

matplot(my_matrix, type ="o", pch=16)

title(xlab= "X Axis", ylab = "Y Axis", main = "RStudio Homework", col.main="Black")

# 2. Write a R program to create a Data frames which contain 
#    details of 5 employees and display the details. (Name, Age, Role and Length of service).

employeesDataSet = data.frame(Name=c("Ana E","Bobby B","Kathie F", "John R","Martin G"),
                       Age=c(22,19,28,45,32),
                       Designation=c("Data Engineer","Product Manager","Software Developer","Full Stack Developer","Web Developer"),
                       LengthOfService=c("1 Year","6 Months","6 Years","32 Years","10 Years")
)
print("Employee Details: ")                      
print(employeesDataSet)

# 3. - Import the GGPLOT 2 library and plot a graph using the qplot function. 
#    - X axis is the sequence of 1:20 and the y axis is the x ^2. 
#    - Label the graph appropriately. 
#    - install.packages("ggplot2", dependencies = TRUE).

install.packages("ggplot2")
library(ggplot2)

data(package = "ggplot2")

xaxis <- 1:20; yaxis = xaxis ^ 2

qplot(xaxis, yaxis, geom = c("point", "line"), main = "RStudio Homework")


# 4. Create a simple bar plot of five subjects.
df <- data.frame(Subject=c("Maths", "English", "Computer Science"),
                 Rating=c(4.2, 10, 29.5))

# Plot data and customize design
p <- ggplot(data=df, aes(x=Subject, y=Rating, fill=Subject)) +
  geom_bar(stat="identity")+
  geom_text(aes(label=Rating), vjust=-0.3, size=3.5) + ggtitle("RStudio Homework")

p + coord_flip()


# -------------------------------------Extension

# 5. Write a R program to take input from the user (name and age) and display the values. 

name = readline(prompt="What is your name: ")

age =  readline(prompt="What is your age: ")

print(paste("My name is",name, "and I am",age ,"years old."))

print(R.version.string)


# 6. Write a R program to create a sequence of numbers from 20 to 50 and find the mean 
#    of numbers from 20 to 50 and sum of numbers.

print("Sequence of numbers from 20 to 50:")
print(seq(20,50))

print("Mean of numbers from 20 to 50:")
print(mean(20:50))

print("Sum of numbers from 20 to 50:")
print(sum(20:50))

# 7. Write a R program to create a vector which contains 10 
#    random integer values between -50 and +50.

vectornumbers = sample(-50:50, 10, replace=TRUE)

print("Vector Content:")

print("Random Numbers between -50 and +50:")

print(vectornumbers)


# -------------------------------------Additional Tasks

# 1. Write a R program to get the first 10 Fibonacci numbers.

fibonaccinumbers <- numeric(10)

fibonaccinumbers[1] <- fibonaccinumbers[2] <- 1

for (i in 3:10) fibonaccinumbers[i] <- fibonaccinumbers[i - 2] + fibonaccinumbers[i - 1]

print("First 10 Fibonacci numbers:")

print(fibonaccinumbers)


# 2. Write a R program to print the numbers from 1 to 100 
# and print "Fizz" for multiples of 3, print "Buzz" for 
# multiples of 5, and print "FizzBuzz" for multiples of 
# both.

# Method 1 of doing Fizz buzz

install.packages("fizzbuzzR")

library(fizzbuzzR)

fizzbuzz(start = 1, end = 100, step = 1, mod1 = 3, mod2 = 5)

# Method 2 of doing Fizz buzz

fizzbuzznumbers <- 1:100
output <- vector()

for (i in fizzbuzznumbers) {
  output[i] <- ""
  
  if (i %% 3 == 0) {output[i] <- paste0(output[i], "Fizz")}
  if (i %% 5 == 0) {output[i] <- paste0(output[i], "Buzz")}
  if (output[i] == "") {output[i] <- i}
}

print(output)



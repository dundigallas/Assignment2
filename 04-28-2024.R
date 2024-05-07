# Load required library
library(ggplot2)

# Generate random data
First <- rnorm(50)
Second <- First + rnorm(50, mean = 0, sd = 0.4)
data <- as.data.frame(cbind(First, Second))

# Summary of the data
summary(data)

# Visualization
ggplot(data, aes(x = First, y = Second)) +
  geom_point(size = 2)

# Load anscombe dataset and visualize
data("anscombe"); #semicolon added
levels <- gl(4, nrow(anscombe))
mydata <- with(anscombe, data.frame(x = c(x1, x2, x3, x4), y = c(y1, y2, y3, y4), mygroup = levels))
theme_set(theme_bw())
ggplot(mydata, aes(x, y)) +
  geom_point(size = 4) +
  geom_smooth(method = "lm", fill = NA, fullrange = TRUE) +
  facet_wrap(~mygroup)

# Define matrices
A <- matrix(1:10, nrow = 5)
B <- matrix(21:40, nrow = 2)
C <- matrix(1:100, nrow = 20)
D <- matrix(0, 4, 4)
E <- matrix(0, 10)
F <- matrix(c(4, 5, 6, 2, 3, 4, 12, 34, 45, 10, 55, 32), 4, 3)

# Matrix operations
Data <- 1:20
A <- matrix(Data, 4, 5)
B <- matrix(Data, 4, 5, byrow = TRUE)
C <- A + B

# Define vectors
r1 <- c("I", "am", "happy")
r2 <- c("what", "a", "day")
r3 <- 1:3
C <- rbind(r1, r2, r3) #each one becomes a Row
D <- cbind(r1, r2, r3)

# Matrix indexing
A <- matrix(1:10, nrow = 5)
A[1, 1]
A[, 1]
A[1, ]
A[-2, ]
A[, -2]
A[-2, -2]

# Named vector
Charlie <- 7:11
names(Charlie) <- c("a", "b", "c", "d", "e")
Charlie
Charlie[4]
Charlie["d"]
names(Charlie)
names(Charlie) <- NULL
Charlie

# Matrix row and column names
temp <- rep(c("a", "b", "c"), each = 3)
Bravo <- matrix(temp, 3, 3)
rownames(Bravo) <- c("Tom", "Dick", "Harry")
colnames(Bravo) <- c("Alice", "Jane", "Mary")

# Subsetting matrices and vectors
x <- c("a", "b", "c", "d", "e")
x[c(1, 4)]
x[1]

# Visualization of data not defined in the script
# You need to define or load these data frames before using them
# matplot and myplot functions are not defined in this script

# Additional code that uses undefined objects should be fixed or removed

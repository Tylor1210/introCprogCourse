#Goal: Learn to use for loops to iterate over numbers.

#Assignment: Assume the variable n has been assigned a positive integer. Write a code fragment that calculates the sum of the even numbers from 1 through n. Use a for loop in your code and assign the sum to a variable named sum_even.

sum_even = 0
for x in range (0, n + 1, 2):
    sum_even += x

Unit 3.1 Quiz If statement
Q311
Goal: Learn how to use boolean expressions and store their value.

Assignment: Write a boolean expression that is True if and only if x is equal to hello and assign its value to the variable check. Assume that x has already been assigned.
check = (x == "hello")

Q312
Goal: Learn to use control flows to obtain conditional results.

Assignment: Assume the variable x has been assigned a float. Write a piece of code that assigns the absolute value of x to value. You cannot use the built-in function abs.
if(x > 0):
    value = x
else:
    value = (x * -1)

Note: The absolute value of a number is the number without the sign.

Q313
Goal: Learn to use control flows to obtain conditional results.

Assignment: Assume the variables x and y have been assigned different integer values. Write a fragment of code that assigns the least of these two variables to another variable named lesser.
if(x > y):
    lesser = y
elif(y > x):
    lesser = x

Q314
Goal: Learn to use control flows to apply conditional effects.

Assignment: Assume guillotine has been assigned a positive integer value. Write an if statement that halves the value of guillotine if its current value is even.
if ((guillotine % 2) == 0):
    guillotine = (guillotine / 2)

Unit 3.2 Quiz
Goal: Learn to use the if-else statement to encode mutually exclusive behavior.

Assignment: Assume that the variable year is assigned a positive integer value. Write an if-else statement that assigns to days 366 if year is a leap year, otherwise, it assigns 365 to days.

Note: Assume any year that is divisible by 4 with no remainder is a leap year.

Question
Assume the variable s has been assigned a string. Write code that displays "stop" if s is equal to "end". Otherwise, display "go".
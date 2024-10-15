#Question
#Write a program that lets the user enter a series of numbers and calculates the sum of all the numbers entered.

#The program should start by asking "How many numbers do you have?". The user enters a number, and the program executes a loop that iterates that many times. Each time the loop iterates, it should prompt the user to enter a number. After all the numbers have been entered, the program should display the sum of the numbers.

#Below are two sample runs of the program. In the first sample run, the user enters five numbers, and in the second sample run, the user enters 3 numbers. Your program’s output must exactly match the output shown in the sample runs. Notice the wording of the messages and the placement of spaces and punctuation. 

#Sample Run (with user input shown between <>):
def main():
    sum_num = 0 
    num = int(input("How many numbers do you have?"))
    for i in range(num):
        total = int(input("Enter a number: "))
        sum_num += total
    
        
    print("Sum: ", sum_num)

main()
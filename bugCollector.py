#this is an example of a loop that requests info for 7 different intervals
# adds them up ad prints the result 
def main():
    total = 0

    for day in range(1, 8):
        print("Enter the bugs collected on day", day)
        bugs = int(input())
        total += bugs

    print(f'You collected a total of {total} bugs')

main()

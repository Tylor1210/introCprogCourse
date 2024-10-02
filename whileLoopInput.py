def main():
    #Input
    #input() returns str, need int()
    num = int(input("What number do you want a Multiplication table for?: "))
    isContinue = True
    cnt = int(1)


    while (isContinue):
        print(f" {num} x {cnt} = ", int(num * cnt))
        cnt = cnt + 1
        
        if(cnt > 10):
            isContinue = False
main()
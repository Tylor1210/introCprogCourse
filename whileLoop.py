def main():
    print("Multiplication Table for #2's")
    isContinue = True
    cnt = 1

    while (isContinue):
        print(" 2 x " + str(cnt) + " = " + str((2 * cnt)))
        cnt = cnt + 1
        if(cnt > 10):
            isContinue = False
main()
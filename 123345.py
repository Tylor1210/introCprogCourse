def main():
    color1 = input("Enter the first color: ")
    color2 = input("Enter the second color: ")
    if(color1 or color2 != "green","red", "yellow", "orange", "blue", "purple"):
        print("You did not enter one of red, orange, yellow, green, blue or purple")
    elif(color1 == "yellow" or "purple" and  color2 == "yellow" or "purple"):
        print("The two colors are complementary")
    elif(color1 == "blue" or "orange" and  color2 == "blue" or "orange"):
        print("The two colors are complementary")
    elif(color1 == "red" or "green" and  color2 == "red" or "green"):
        print("The two colors are complementary")
    

main()

def search101():
    entered_nums = []
    num1 = input("Enter the 1st number: ")
    entered_nums.append(num1)
    num2 = input("Enter the 2nd number: ")
    entered_nums.append(num2)
    num3 = input("Enter the 3rd number: ")
    entered_nums.append(num3)
    num4 = input("Enter the 4th number: ")
    entered_nums.append(num4)
    num5 = input("Enter the 5th number: ")
    entered_nums.append(num5)
    last_num = input("Enter the last number: ")
    if last_num in entered_nums:
        print(f"{last_num} is in {num1},{num2},{num3},{num4},{num5}.")
    else:
        print(f"{last_num} isn't in {num1},{num2},{num3},{num4},{num5}.")

search101()

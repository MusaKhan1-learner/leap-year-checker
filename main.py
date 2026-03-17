year = int(input("Which year do you want to check"))
if year % 4 == 0:
    print(f"THe {year} is leap year")
    if year % 100 == 0:
        print(f"The year {year}is not leap year")
        if year % 400 == 0:
            print(f"the year{year} is a leap year ")
else:
    print(f"The year {year} is not a leap year")

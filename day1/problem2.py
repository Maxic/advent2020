def main():
    expenses_found = False

    with open("input.txt", "r+") as file:
        content = file.readlines()

        expenses = [int(expense) for expense in content]
        expenses.sort()
        for i in expenses:
            if expenses_found: break
            for j in expenses:
                if expenses_found: break
                for k in expenses:
                    if i+j+k == 2020:
                        print(i*j*k)
                        expenses_found = True
                        break


if __name__ == "__main__":
    main()


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        expenses = [int(expense) for expense in content]

        for expense in expenses:
            leftover = 2020-expense
            if leftover in expenses:
                print(leftover*expense)
                break


if __name__ == "__main__":
    main()


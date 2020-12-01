def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        expenses = [int(expense) for expense in content]

        # expenses is een lijst van getallen
        print(expenses)
        for expense in expenses:
            leftover = 2020-expense
            if expenses.__contains__(leftover):
                print(leftover*expense)
                break


if __name__ == "__main__":
    main()


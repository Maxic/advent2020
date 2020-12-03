def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        expenses = [int(expense) for expense in content]
        expenses.sort()

        index = 1
        pairs = []

        # create an array with all possible pairings
        for i in expenses:
            index += 1
            for j in range(index, expenses.__len__()):
                pairs.append((i, expenses[j]))

        # check what 3 numbers add up to 2020
        for pair in pairs:
            leftover = 2020 - (pair[0] + pair[1])
            if leftover in expenses:
                print(leftover * pair[0] * pair[1])
                break


if __name__ == "__main__":
    main()


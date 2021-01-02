def main():

    with open("input.txt", "r+") as file:
        joltages = [int(line.strip()) for line in file.readlines()]

        initial_joltage = 0
        distribution = {1: 0, 3: 0}

        while joltages.__len__() > 0:
            next_joltage = min(joltages)
            joltage_diff = next_joltage - initial_joltage
            distribution[joltage_diff] += 1

            initial_joltage = next_joltage
            joltages.remove(next_joltage)

        # Don't forget the built-in adapter
        distribution[3] += 1

        print(distribution[1] * distribution[3])


if __name__ == "__main__":
    main()

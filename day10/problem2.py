def main():

    with open("test.txt", "r+") as file:
        joltages = [int(line.strip()) for line in file.readlines()]

        initial_joltage = 0
        possibly_unused_joltages = []
        joltages.sort()

        for joltage in joltages:
            if joltage == initial_joltage + 3:
                initial_joltage = joltage
                continue
            if joltage == initial_joltage + 2:
                if not joltages.__contains__(initial_joltage+3):
                    initial_joltage = joltage
                    continue
            if joltage == initial_joltage + 1:
                if not joltages.__contains__(initial_joltage+3) and not joltages.__contains__(initial_joltage+2):
                    initial_joltage = joltage
                    continue

            initial_joltage = joltage
            possibly_unused_joltages.append(joltage)

        print(possibly_unused_joltages)


if __name__ == "__main__":
    main()

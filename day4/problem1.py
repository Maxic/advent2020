def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        [print(line) for line in content]


if __name__ == "__main__":
    main()


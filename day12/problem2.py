def main():

    with open("input.txt", "r+") as file:
        content = [line.strip for line in file.readlines()]


if __name__ == "__main__":
    main()

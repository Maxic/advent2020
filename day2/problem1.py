def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        for item in content:
            print(item)
            print('test')


if __name__ == "__main__":
    main()

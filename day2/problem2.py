def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        valid_password_count = 0

        for item in content:
            parameters = item.split(' ')
            range = parameters[0]
            index1 = int(range.split('-')[0])-1
            index2 = int(range.split('-')[1])-1
            letter = parameters[1][0]
            password = parameters[2].strip()

            count_on_index = 0

            if password[index1] == letter: count_on_index += 1
            if password[index2] == letter: count_on_index += 1

            if count_on_index == 1:
                valid_password_count += 1

        print(valid_password_count)


if __name__ == "__main__":
    main()

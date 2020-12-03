def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        valid_password_count = 0

        for item in content:
            parameters = item.split(' ')
            range = parameters[0]
            low_value = int(range.split('-')[0])
            high_value = int(range.split('-')[1])
            letter = parameters[1][0]
            password = parameters[2].strip()

            letter_occurrence = password.count(letter)

            if low_value <= letter_occurrence <= high_value:
                valid_password_count += 1

        print(valid_password_count)


if __name__ == "__main__":
    main()
